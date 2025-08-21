# =============================
# guardrails.py  — FULL FILE (patched)
# =============================
from __future__ import annotations
import re
import math
from typing import Dict, List, Tuple, Any

# -----------------------------
# Helpers
# -----------------------------

_STOPWORDS = {
    "the","a","an","and","or","but","if","then","else","when","so","because",
    "of","in","on","at","to","for","from","by","with","about","as","into","like","through",
    "is","are","was","were","be","been","being","do","does","did","doing",
    "that","this","these","those","it","its","it's","i","you","he","she","we","they","them",
    "your","yours","his","her","their","our","ours","me","my","mine",
    "not","no","nor","too","very","can","cannot","can't","could","should","would","will","won't",
    "than","up","down","over","under","again","further","then","once","here","there","all","any","both",
    "each","few","more","most","other","some","such","only","own","same","so","too","very","s","t","just",
    "also","via","per"
}

_REFUSAL_PATTERNS = [
    r"i (?:can(?:not|n't)|do not|don't) answer",
    r"i (?:can(?:not|n't)|do not|don't) help with that",
    r"insufficient (?:context|information)",
    r"no (?:information|context) provided",
    r"the provided context (?:does not|doesn't) contain",
    r"i (?:don'?t|cannot) have access to",
    r"as an ai (?:language )?model, i (?:cannot|can't)",
    r"i (?:cannot|can't) comply",
    r"unable to (?:answer|comply)",
    r"out of scope",
]

def _normalize_text(s: str) -> str:
    s = s.strip().lower()
    # collapse whitespace
    s = re.sub(r"\s+", " ", s)
    return s

def _sent_tokenize(s: str) -> List[str]:
    s = _normalize_text(s)
    parts = re.split(r"[\.!?;\n•]+", s)
    return [p.strip() for p in parts if len(p.strip()) >= 3]

def _word_tokens(s: str) -> List[str]:
    return re.findall(r"[a-z0-9]+", s.lower())

def _content_words(s: str, min_len: int = 5) -> List[str]:
    return [w for w in _word_tokens(s) if len(w) >= min_len and w not in _STOPWORDS]

def _dice_coefficient(a_tokens: List[str], b_tokens: List[str]) -> float:
    """
    Sørensen–Dice coefficient on token sets.
    Returns 0..1. Robust to length mismatch and word order.
    """
    if not a_tokens or not b_tokens:
        return 0.0
    A, B = set(a_tokens), set(b_tokens)
    overlap = len(A & B)
    if overlap == 0:
        return 0.0
    return 2.0 * overlap / (len(A) + len(B))

# -----------------------------
# Guardrail 1: Cheap Recall
# -----------------------------

def cheap_recall_coverage(reference_answer: str, contexts: List[str] | str,
                          sentence_match_threshold: float = 0.62,
                          min_words_per_sentence: int = 3) -> Tuple[float, int, int]:
    if isinstance(contexts, str):
        contexts = [contexts]
    # Concatenate all contexts to simplify; this is a *cheap* proxy metric.
    ctx_concat = " ".join(contexts)
    ctx_tokens = _word_tokens(ctx_concat)

    ref_sents = _sent_tokenize(reference_answer)
    # Filter out very short/noisy sentences
    filtered = [s for s in ref_sents if len(_word_tokens(s)) >= min_words_per_sentence]
    total = len(filtered)

    if total == 0:
        # Fallback: treat the whole reference as one chunk
        sim = _dice_coefficient(_word_tokens(reference_answer), ctx_tokens)
        matched = 1 if sim >= (sentence_match_threshold * 0.85) else 0
        total = 1
        return (matched / total, matched, total)

    # [ADDED] Normal path: compute matches & return coverage
    matched = 0
    for s in filtered:
        sim = _dice_coefficient(_word_tokens(s), ctx_tokens)
        if sim >= sentence_match_threshold:
            matched += 1
    coverage = matched / total if total else 0.0
    return (coverage, matched, total)


def bump_context_recall_if_applicable(current_context_recall: int,
                                      coverage_ratio: float,
                                      high_coverage_threshold: float = 0.85,
                                      bump_mode: str = "to_derived") -> int:
    """
    If cheap recall coverage is high but the judge scored context_recall too low, bump it.

    bump_mode:
      - "to_derived": set to round(10 * coverage_ratio) if that is higher.
      - "to_10_when_very_high": set to 10 if coverage_ratio >= 0.90; else keep current.

    Returns the possibly adjusted context_recall (0..10).
    """
    derived = int(round(10 * coverage_ratio))
    if coverage_ratio >= high_coverage_threshold:
        if bump_mode == "to_derived":
            return max(current_context_recall, derived)
        elif bump_mode == "to_10_when_very_high" and coverage_ratio >= 0.90:
            return max(current_context_recall, 10)
    return current_context_recall

# -----------------------------
# Guardrail 2: Refusal Override Flag
# -----------------------------

def is_refusal(prediction: str,
               refusal_strings: List[str] | None = None,
               refusal_regexes: List[str] | None = None) -> bool:
    """
    Detect obvious refusals.

    - Exact/near-exact string matches (after normalization)
    - Regex patterns capturing common refusal phrasings
    """
    norm = _normalize_text(prediction)
    if refusal_strings:
        for rs in refusal_strings:
            if _normalize_text(rs) == norm:
                return True
    # regex scan
    patterns = refusal_regexes if refusal_regexes is not None else _REFUSAL_PATTERNS
    for pat in patterns:
        if re.search(pat, norm):
            return True
    return False


def question_keywords_present_in_context(question: str, contexts: List[str] | str,
                                         min_overlap: int = 1) -> bool:
    if isinstance(contexts, str):
        contexts = [contexts]
    q_kw = set(_content_words(question))
    if not q_kw:
        return False
    ctx_text = " ".join(contexts).lower()
    hits = 0
    for w in q_kw:
        if w in ctx_text:
            hits += 1
            if hits >= min_overlap:
                return True
    return False

# -----------------------------
# Orchestrator: Apply Both Nets
# -----------------------------

def apply_safety_nets(
    question: str,
    contexts: List[str] | str,
    reference_answer: str,
    prediction: str,
    judge_scores: Dict[str, Any],
    config: Dict[str, Any] | None = None,
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """
    Apply the two safety nets to `judge_scores` and return (adjusted_scores, flags).

    Inputs:
      - judge_scores must contain integer 0..10 for keys:
        ["faithfulness", "answer_relevancy", "context_precision", "context_recall", "answer_correctness"]

    Flags returned:
      {
        "cheap_recall": {"coverage": float, "matched": int, "total": int, "bumped": bool, "examples": [...]},
        "refusal": {"flagged": bool, "reason": str}
      }
    """
    cfg = config or {}
    # --- Cheap Recall ---
    cr_enable = cfg.get("cheap_recall_enable", True)
    cr_sent_thr = float(cfg.get("cheap_recall_sentence_threshold", 0.58))
    cr_min_words = int(cfg.get("cheap_recall_min_words", 3))
    cr_high_cov_thr = float(cfg.get("cheap_recall_high_coverage_threshold", 0.85))
    cr_bump_mode = cfg.get("cheap_recall_bump_mode", "to_derived")

    flags = {"cheap_recall": {"coverage": 0.0, "matched": 0, "total": 0, "bumped": False},
             "refusal": {"flagged": False, "reason": ""}}
    adjusted = dict(judge_scores)

    if cr_enable:
        cov, matched, total = cheap_recall_coverage(
            reference_answer, contexts,
            sentence_match_threshold=cr_sent_thr,
            min_words_per_sentence=cr_min_words
        )
        flags["cheap_recall"].update({"coverage": cov, "matched": matched, "total": total})

        # [ADDED] Tiny sampling for auditability — this is where it was supposed to go
        try:
            ref_sents = _sent_tokenize(reference_answer)
            ctx_text = " ".join(contexts) if isinstance(contexts, list) else contexts
            ctx_tokens = _word_tokens(ctx_text)
            examples = []
            for s in ref_sents[:3]:
                sim = _dice_coefficient(_word_tokens(s), ctx_tokens)
                examples.append({"sent": s[:100], "sim": round(sim, 3)})
            flags["cheap_recall"].update({"examples": examples})
        except Exception:
            pass

        new_recall = bump_context_recall_if_applicable(
            int(adjusted.get("context_recall", 0)), cov,
            high_coverage_threshold=cr_high_cov_thr,
            bump_mode=cr_bump_mode
        )
        if new_recall != adjusted.get("context_recall", 0):
            adjusted["context_recall"] = new_recall
            flags["cheap_recall"]["bumped"] = True

    # --- Refusal Override Flag ---
    ro_enable = cfg.get("refusal_override_enable", True)
    if ro_enable:
        refusal_strings = cfg.get("refusal_strings", [])
        refusal_regexes = cfg.get("refusal_regexes", None)
        keyword_overlap = int(cfg.get("refusal_keyword_min_overlap", 1))
        mark_review_only = bool(cfg.get("refusal_mark_review_only", True))
        if is_refusal(prediction, refusal_strings=refusal_strings, refusal_regexes=refusal_regexes):
            if question_keywords_present_in_context(question, contexts, min_overlap=keyword_overlap):
                flags["refusal"]["flagged"] = True
                flags["refusal"]["reason"] = (
                    "Model refused despite overlap between question keywords and retrieved context."
                )
                if not mark_review_only:
                    # Aggressive option: penalize faithfulness and relevancy since refusal was unwarranted.
                    adjusted["faithfulness"] = 0
                    adjusted["answer_relevancy"] = min(adjusted.get("answer_relevancy", 0), 2)

    return adjusted, flags


def debug_cheap_recall(reference_answer: str, contexts: List[str] | str):
    # [ADDED] Utility for manual debugging — this is where it was supposed to go
    if isinstance(contexts, str):
        contexts = [contexts]
    ctx_concat = " ".join(contexts)
    ctx_tokens = _word_tokens(ctx_concat)
    for s in _sent_tokenize(reference_answer):
        sim = _dice_coefficient(_word_tokens(s), ctx_tokens)
        print(f"[cheap_recall] sent='{s[:80]}...'  sim={sim:.3f}")