# benchmark.py — shardable, resumable; captures final_context exactly

import os
import time
import json
import logging
import argparse
from tqdm import tqdm
import hashlib
import re
import rag_pipeline as rag
from config import CONFIG

# --- Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def make_row_id(row):
    """Creates a stable row ID from the row's 'id' field, or a hash of the question."""
    if row.get("id"):
        return str(row["id"])
    q = re.sub(r"\s+", " ", row["question"]).strip().lower()
    return hashlib.sha1(q.encode("utf-8")).hexdigest()[:16]


def load_jsonl(path: str):
    """Loads a JSONL file, skipping malformed lines."""
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError:
                logging.error(f"Skipping malformed JSONL line {i} in {path}")
    return data


def main():
    """
    PHASE 1: Generate answers and capture metrics via synchronous RAG pipeline.
    Supports sharded datasets and resumable checkpoints.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", default=CONFIG.BENCHMARK_DATASET_PATH,
                        help="Path to JSONL benchmark dataset (one item per line)")
    parser.add_argument("--out", default=CONFIG.GENERATED_ANSWERS_CHECKPOINT,
                        help="Path to append JSONL generated answers checkpoint")
    parser.add_argument("--sleep", type=float, default=CONFIG.API_SLEEP_INTERVAL,
                        help="Sleep between items to smooth rate limits")
    args = parser.parse_args()

    print("--- RAG Benchmark: Answer Generation ---")

    # --- Load dataset ---
    if not os.path.exists(args.dataset):
        logging.error(f"Benchmark file not found at '{args.dataset}'.")
        return
    benchmark_data = load_jsonl(args.dataset)
    if not benchmark_data:
        logging.error(f"Benchmark file '{args.dataset}' is empty or invalid.")
        return

    # --- Resumable checkpointing ---
    processed_ids = set()
    if os.path.exists(args.out):
        with open(args.out, "r", encoding="utf-8") as f:
            processed_ids = {json.loads(l).get("row_id") for l in f if l.strip()}
    logging.info(f"Found {len(processed_ids)} previously processed question IDs.")

    questions_to_process = [r for r in benchmark_data if make_row_id(r) not in processed_ids]
    if not questions_to_process:
        logging.info("All questions already processed. Proceed to judging.")
        return

    # --- Init systems once ---
    logging.info("Initializing RAG pipeline systems...")
    systems = rag.initialize_systems()
    logging.info("✅ AI Systems Initialized.")

    class DummySessionState:
        def __init__(self):
            self.last_retrieved_context = None

    # --- Process ---
    with open(args.out, "a", encoding="utf-8") as f:
        for row in tqdm(questions_to_process, desc="Generating Answers"):
            question = row["question"]
            row_id = make_row_id(row)
            session_state = DummySessionState()
            history = []  # empty for benchmarking

            try:
                start = time.time()
                pipeline_response = rag.run_full_pipeline(
                    user_input=question,
                    chat_history=history,
                    systems=systems,
                    update_callback=lambda msg: None,
                    session_state=session_state,
                )
                latency_ms = round((time.time() - start) * 1000)

                # Stream -> string
                answer_stream = pipeline_response.get("stream", [])
                if not isinstance(answer_stream, (list, tuple)):
                    # allow generator
                    answer = "".join(list(answer_stream))
                else:
                    answer = "".join(answer_stream)

                # Sources/contexts
                docs = pipeline_response.get("sources", []) or []
                contexts = [d.page_content for d in docs if hasattr(d, 'page_content')]

                # Optional refusal override
                if hasattr(rag, "is_refusal") and hasattr(rag, "question_keyword_overlap_with_context") and hasattr(rag, "retry_force_answer"):
                    try:
                        if rag.is_refusal(answer) and rag.question_keyword_overlap_with_context(question, contexts):
                            retry = rag.retry_force_answer(question, history, systems, docs)
                            if retry and retry.get("answer"):
                                answer = retry["answer"]
                    except Exception as e:
                        logging.warning(f"Refusal-override skipped: {e}")

                # Freeze the exact final context used by the generator
                final_context = pipeline_response.get("final_context", "")

                result_item = {
                    "row_id": row_id,
                    "model": CONFIG.PRIMARY_LLM_MODEL,
                    "question": question,
                    "answer": answer,
                    "contexts": contexts,
                    "final_context": final_context,
                    "ground_truth_context": row.get("ground_truth_context", []),
                    "ground_truth_answer": row.get("ground_truth_answer", ""),
                    "latency_ms": latency_ms,
                }
                f.write(json.dumps(result_item, ensure_ascii=False) + "\n")
                f.flush()

            except Exception as e:
                logging.error(f"Error processing question: '{question[:80]}...' -> {e}", exc_info=True)
                continue

            time.sleep(args.sleep)

    logging.info("Answer generation complete.")


if __name__ == "__main__":
    main()
