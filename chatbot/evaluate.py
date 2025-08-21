import os
import re
import csv
import json
import time
import hashlib
import logging
import argparse
from typing import Set, List, Dict, Any
import random
import pandas as pd
from tqdm import tqdm
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from config import CONFIG

# Optional guardrails (safe if missing in your env)
try:
    from guardrails import apply_safety_nets  # your local util
except Exception:
    def apply_safety_nets(**kwargs):
        return kwargs.get("judge_scores", {}), {"cheap_recall": {}, "refusal": {}}

# --- Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# =========================
# Backoff utilities
# =========================

def call_with_backoff(fn, *args, **kwargs):
    """
    Wrap a single Groq call. Retries on rate limits / transient server errors
    with exponential backoff + jitter. Returns the function result or re-raises.
    """
    base = 0.75   # baseline delay for first retry
    cap  = 20.0   # max backoff seconds
    attempts = 5  # total tries

    for i in range(1, attempts + 1):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            msg = str(e).lower()
            is_rate = "rate_limit" in msg or "tpm" in msg or "429" in msg
            is_server = " 500" in msg or " 503" in msg
            is_payload = "payload too large" in msg or "413" in msg

            if is_payload:
                # Sleep will not help a 413 — trim your prompt/context before retrying.
                raise

            if not (is_rate or is_server) or i == attempts:
                # Not a retriable error, or we've exhausted retries
                raise

            # Exponential backoff with jitter
            delay = min(cap, base * (2 ** (i - 1)) + random.uniform(0, 0.5))
            time.sleep(delay)

def smooth_sleep(base: float = 0.5, jitter: float = 0.3):
    """Light smoothing between rows to avoid burstiness."""
    time.sleep(max(0.0, base) + random.uniform(0, max(0.0, jitter)))

# =========================
# Robust JSON Sanitization
# =========================

VALID_ESCAPES = r'\\|/|"|b|f|n|r|t|u'  # legal JSON escape chars after a backslash

def _strip_code_fences(s: str) -> str:
    s = s.strip()
    s = re.sub(r"^```(?:json)?\s*", "", s, flags=re.IGNORECASE)
    s = re.sub(r"\s*```$", "", s)
    return s

def _normalize_quotes(s: str) -> str:
    return (s
            .replace("\u201c", '"').replace("\u201d", '"')  # “ ”
            .replace("\u2018", "'").replace("\u2019", "'")) # ‘ ’

def _fix_invalid_backslashes(s: str) -> str:
    # Turn \x into \\x unless x is a valid JSON escape char
    return re.sub(r'\\(?!' + VALID_ESCAPES + r')', r'\\\\', s)

def _remove_trailing_commas(s: str) -> str:
    # ,] or ,} -> ] or }
    return re.sub(r',\s*([}\]])', r'\1', s)

def extract_and_sanitize_json(text: str) -> str:
    """Extract the outermost { ... } and sanitize it into parseable JSON."""
    text = _strip_code_fences(_normalize_quotes(text))
    start = text.find('{')
    end = text.rfind('}')
    if start == -1 or end == -1 or end <= start:
        raise json.JSONDecodeError("No valid JSON object found", text, 0)
    blob = text[start:end+1]
    blob = _fix_invalid_backslashes(blob)
    blob = _remove_trailing_commas(blob)
    return blob

# =========================
# Safe JSONL ingestion
# =========================

def _sanitize_jsonl_line(line: str) -> str:
    # Try to salvage a single JSONL object line by fixing quotes, backslashes, commas.
    s = line.strip()
    if not s:
        return s
    s = _normalize_quotes(s)
    s = _fix_invalid_backslashes(s)
    s = _remove_trailing_commas(s)
    return s

def read_jsonl_safely(path: str):
    """Yield dict rows from a JSONL file, attempting repair on bad lines and logging offenders."""
    with open(path, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            raw = line.rstrip("\n")
            if not raw:
                continue
            try:
                yield json.loads(raw)
            except json.JSONDecodeError as e1:
                fixed = _sanitize_jsonl_line(raw)
                try:
                    yield json.loads(fixed)
                    logging.warning(f"Recovered malformed JSON on line {lineno} of {path}: {e1}")
                except Exception as e2:
                    snippet = raw[max(0, (getattr(e1, 'pos', 0) or 0) - 80): (getattr(e1, 'pos', 0) or 0) + 80]
                    logging.error(f"Unrecoverable JSON on line {lineno} of {path}: {e2}\nSnippet: {snippet}")
                    continue

# =========================
# Helpers
# =========================

def row_id_from_question(q: str) -> str:
    """Stable row ID from question text (case/whitespace-insensitive)."""
    qn = re.sub(r"\s+", " ", (q or "")).strip().lower()
    return hashlib.sha1(qn.encode("utf-8")).hexdigest()[:16]

def is_tpd_error(exc: Exception) -> bool:
    """Heuristic check for Groq daily Tokens-Per-Day type errors."""
    msg = str(exc).lower()
    return ("tokens per day" in msg) or ("rate_limit_exceeded" in msg and ("tpm" in msg or "tpd" in msg))

def load_existing_ids(out_csv: str) -> Set[str]:
    """Load existing row_ids from the output CSV to allow resume without duplicates."""
    if not os.path.exists(out_csv):
        return set()
    ids: Set[str] = set()
    with open(out_csv, "r", encoding="utf-8", newline="") as f:
        try:
            rdr = csv.DictReader(f)
            for r in rdr:
                rid = r.get("row_id")
                if rid:
                    ids.add(rid)
        except Exception:
            pass
    return ids

def open_writer(out_csv: str):
    """Open a CSV writer, creating the header if the file is new."""
    exists = os.path.exists(out_csv)
    f = open(out_csv, "a", encoding="utf-8", newline="")
    fieldnames = [
        "row_id", "model", "question", "answer",
        "faithfulness", "answer_relevancy", "context_precision", "context_recall", "answer_correctness",
        "judge_model_used", "evaluation_status", "reasoning", "flags"
    ]
    w = csv.DictWriter(f, fieldnames=fieldnames)
    if not exists:
        w.writeheader()
    return f, w

# =========================
# Judge prompt with strict formatting guardrails
# =========================
EVALUATION_PROMPT_TEMPLATE = r"""
SYSTEM: You are a rigorous, adversarial RAG evaluator. Produce fair, reproducible scores.
Return ONE JSON object with exactly two top-level keys: "reasoning" and "scores".
Do all steps below, but ONLY return the JSON.

[STEP 1: Identify Core Intent]
- Determine the question's intent ∈ [fact, definition, significance, mechanism, comparison, steps, other].
- If the question uses colloquialisms like “what’s the big deal” or asks “why”, set intent=significance.

[STEP 2: Deconstruct the Reference Answer]
- Extract 2–5 concise REF_KEYPOINTS from the Reference Answer.
- Mark exactly one as REF_MAIN_POINT (the single most important takeaway).

[STEP 3: Check Context Sufficiency (Retrieval ONLY)]
- For each REF_KEYPOINT, copy a SHORT, VERBATIM supporting quote (≤20 words) from Context; else mark MISSING.
- Do NOT paraphrase. If you cannot find a verbatim substring, mark MISSING.
- Compute context_recall = round(10 * (#supported / total)).
- If REF_MAIN_POINT is MISSING in Context → cap context_recall at 6.
- Compute context_precision about the Context itself (not the Submission):
  10 if >80% directly useful to answer this Question,
   7 if ~50–80%,
   4 if ~20–50%,
   0 if mostly irrelevant.

[STEP 4: Analyze the Submission (Generation)]
- Extract 2–5 SUBMISSION_KEYPOINTS actually claimed in the Submission.
- List UNSUPPORTED_CLAIMS: claims in the Submission lacking Context support (include a short quote disproving it OR "NO_QUOTE_FOUND").
- Compute answer_correctness = round(10 * (#REF_KEYPOINTS present in Submission / total)).
- If REF_MAIN_POINT is NOT addressed in the Submission → cap answer_correctness at 6.
- Compute faithfulness:
    - If UNSUPPORTED_CLAIMS is empty and no contradictions → 10.
    - If any contradictions or obvious unsupported claims → 10 - min(10, 2 * len(UNSUPPORTED_CLAIMS)).
    - If the Submission refuses despite Context covering ≥1 REF_KEYPOINT → set faithfulness = 0.
    - **Soft-refusal rule:** If the Submission asserts that the context is insufficient (e.g., “the text does not explain…”, “not enough information…”, “insufficient context…”) but Step 3 shows ≥1 supported key point (context_recall ≥ 1), then treat this as a refusal and set faithfulness = 0, and include "soft_refusal" in UNSUPPORTED_CLAIMS.
- Compute answer_relevancy:
    - 10 if the Submission directly addresses the detected intent.
    - If intent=significance and MAIN POINT of significance is not addressed → ≤6.
    - Reduce for off-topic padding or ignoring the question.

[STEP 5: Output JSON (and nothing else)]
    [FORMATTING RULES]
        - Return strictly valid JSON (UTF-8, double-quoted keys/strings).
        - Escape all backslashes in strings as `\\`. For example, write `\\phi` not `\phi`.
        - Do not include code fences, markdown, or commentary outside the JSON.
        - No trailing commas.
        - If no evidence is found, set "evidence" to the literal string "MISSING".
        - Return EXACTLY this structure (numbers are integers 0..10):

{{
  "reasoning": {{
    "intent": "<one of the allowed intents>",
    "reference_key_points": ["...", "..."],
    "reference_main_point": "...",
    "context_support": [
      {{"key_point": "...", "evidence": "short quote" or "MISSING"}}
    ],
    "submission_key_points": ["...", "..."],
    "unsupported_claims": ["...", "..."]
  }},
  "scores": {{
    "faithfulness": <0-10>,
    "answer_relevancy": <0-10>,
    "context_precision": <0-10>,
    "context_recall": <0-10>,
    "answer_correctness": <0-10>
  }}
}}

[DATA]
Question: {question}
Context: {context}
Submission: {prediction}
Reference Answer: {reference}
"""

SOFT_REFUSAL_PHRASES = [
    "does not explain", "doesn’t explain", "doesnt explain",
    "not enough information", "insufficient information", "insufficient context",
    "cannot determine from the context", "can't determine from the context",
    "cannot answer from the provided context",
]


# =========================
# Main
# =========================

def main():
    print("--- RAG Benchmark: Answer Judging ---")

    parser = argparse.ArgumentParser()
    parser.add_argument("--answers", default=CONFIG.GENERATED_ANSWERS_CHECKPOINT,
                        help="Path to generated answers JSONL (from benchmark.py)")
    parser.add_argument("--out", default=CONFIG.FINAL_RESULTS_PATH,
                        help="Path to evaluation CSV (appended + resumable)")
    parser.add_argument("--resume", action="store_true",
                        help="Skip rows already present in OUT by row_id")
    parser.add_argument("--stop_on_tpd", action="store_true",
                        help="Stop immediately if Groq daily Tokens-Per-Day limit is hit")
    parser.add_argument("--sleep", type=float, default=CONFIG.API_SLEEP_INTERVAL,
                        help="Sleep between rows to smooth burst limits (min 0.2s)")
    args = parser.parse_args()

    # LLM & chain
    judge_llm = ChatGroq(
    model_name=CONFIG.JUDGE_LLM_MODEL,
    groq_api_key=CONFIG.GROQ_API_KEY,
    temperature=0,
    model_kwargs={"response_format": {"type": "json_object"}}
)
    evaluation_chain = ChatPromptTemplate.from_template(EVALUATION_PROMPT_TEMPLATE) | judge_llm

    # Resume info
    existing_ids = load_existing_ids(args.out) if args.resume else set()
    fout, writer = open_writer(args.out)

    # --- Read answers robustly ---
    rows = list(read_jsonl_safely(args.answers))
    if not rows:
        logging.error(f"No valid rows read from {args.answers}")
        fout.close()
        return

    for i, row in enumerate(tqdm(rows, desc="Judging Answers"), 1):
        try:
            q = row.get("question", "")
        except AttributeError:
            logging.error(f"Skipping non-dict row at index {i}")
            continue

        if not q:
            logging.error(f"Skipping row {i}: missing question.")
            continue

        # Carry row_id through, backfill if missing
        rid = row.get("row_id") or row_id_from_question(q)
        if rid in existing_ids:
            continue

        # Build judge context (prefer final_context → contexts → GT context)
        contexts_for_judge: List[str] = []
        if row.get("final_context"):
            contexts_for_judge = [row["final_context"]]
        else:
            ctx_list = row.get("contexts") or []
            if isinstance(ctx_list, str):
                ctx_list = [ctx_list]
            ctx_list = [c for c in ctx_list if isinstance(c, str) and c]
            contexts_for_judge = ctx_list[: int(getattr(CONFIG, "TOP_K_TO_LLM", 3))]
            if not contexts_for_judge and row.get("ground_truth_context"):
                gt = row.get("ground_truth_context")
                contexts_for_judge = gt if isinstance(gt, list) else [gt]

        contexts_str = "\n---\n".join([c for c in contexts_for_judge if isinstance(c, str) and c])
        contexts_str = contexts_str[: CONFIG.MAX_CONTEXT_CHARS]

        payload = {
            "question": q,
            "context": contexts_str,
            "prediction": (row.get("answer") or "")[: CONFIG.MAX_ANSWER_CHARS],
            "reference": (row.get("ground_truth_answer") or "")[: CONFIG.MAX_GT_CHARS],
        }

        # Invoke judge with backoff wrapper
        try:
            resp = call_with_backoff(evaluation_chain.invoke, payload)
        except Exception as e:
            if is_tpd_error(e) and args.stop_on_tpd:
                logging.error("Daily token quota hit on Groq judge. Stopping evaluation now.")
                break
            logging.error(f"Judge failed on row {i}: {e}")
            continue

        # --- Robust JSON parsing block ---
        response_text = getattr(resp, "content", str(resp))

        try:
            clean_json_str = extract_and_sanitize_json(response_text)
            evaluation_data = json.loads(clean_json_str)
        except json.JSONDecodeError as e:
            logging.error(f"JSON parse error on row {i}: {e}")
            logging.debug(f"Raw judge response (truncated): {response_text[:2000]}")
            # As a last resort, also strip control chars and try again
            scrubbed = re.sub(r'[\x00-\x1F\x7F]', ' ', clean_json_str if 'clean_json_str' in locals() else response_text)
            try:
                evaluation_data = json.loads(scrubbed)
            except Exception:
                # Fall back to minimal scores so the row is still written
                evaluation_data = {
                    "reasoning": {"unsupported_claims": []},
                    "scores": {
                        "faithfulness": 1,
                        "answer_relevancy": 1,
                        "context_precision": 1,
                        "context_recall": 1,
                        "answer_correctness": 1
                    }
                }

        scores = evaluation_data.get("scores", {}) or {}
        reasoning = evaluation_data.get("reasoning", {}) or {}

        # Optional guardrails step (safe if missing)
        try:
            full_ctx = row.get("contexts")
            full_ctx_list = full_ctx if isinstance(full_ctx, list) else ([full_ctx] if isinstance(full_ctx, str) else [])
            adjusted_scores, flags = apply_safety_nets(
                question=q,
                contexts=full_ctx_list,
                reference_answer=row.get("ground_truth_answer", ""),
                prediction=row.get("answer", ""),
                judge_scores=scores,
                config={}
            )
            scores = adjusted_scores or scores
        except Exception as e:
            logging.debug(f"Guardrails skipped on row {i}: {e}")
            flags = {}

        # Write one row immediately (resumable)
        out_row = {
            "row_id": rid,
            "model": row.get("model", CONFIG.PRIMARY_LLM_MODEL),
            "question": q,
            "answer": row.get("answer", ""),
            "faithfulness": int(scores.get("faithfulness", 1)),
            "answer_relevancy": int(scores.get("answer_relevancy", 1)),
            "context_precision": int(scores.get("context_precision", 1)),
            "context_recall": int(scores.get("context_recall", 1)),
            "answer_correctness": int(scores.get("answer_correctness", 1)),
            "judge_model_used": CONFIG.JUDGE_LLM_MODEL,
            "evaluation_status": "ok",
            "reasoning": json.dumps(reasoning, ensure_ascii=False),
            "flags": json.dumps(flags or {}, ensure_ascii=False),
        }
        writer.writerow(out_row)
        fout.flush()

        # Small throttle to smooth bursts (won’t affect daily limits)
        smooth_sleep(base=max(args.sleep, 0.9), jitter=0.5)

    fout.close()

    # Backfill row_id in final CSV if any missing, then print summary
    try:
        df = pd.read_csv(args.out)
        if "row_id" not in df.columns or df["row_id"].isna().any():
            df["row_id"] = df.apply(lambda r: r.get("row_id") or row_id_from_question(r["question"]), axis=1)
            df.to_csv(args.out, index=False)

        metric_cols = [
            "faithfulness", "answer_relevancy", "context_precision", "context_recall", "answer_correctness"
        ]
        summary = df.groupby("model")[metric_cols].mean().reset_index()
        print("\n--- Average Quality Scores per Model (Scale 0-10) ---")
        print(summary.to_markdown(index=False))
    except Exception as e:
        logging.warning(f"Could not compute summary: {e}")


if __name__ == "__main__":
    main()
