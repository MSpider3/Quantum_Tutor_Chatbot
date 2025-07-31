# generate_answers.py
import os
import time
import json
import logging
from tqdm import tqdm
import rag_pipeline as rag
from config import CONFIG
from langchain_core.messages import HumanMessage, AIMessage

# --- Professional-Grade Setup ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Configuration from CONFIG object ---
BENCHMARK_PATH = CONFIG.BENCHMARK_DATASET_PATH
CHECKPOINT_PATH = CONFIG.GENERATED_ANSWERS_CHECKPOINT
API_SLEEP_INTERVAL = CONFIG.API_SLEEP_INTERVAL

def main():
    print("--- Phase 1: Answer Generation ---")

    try:
        with open(BENCHMARK_PATH, 'r', encoding='utf-8') as f:
            benchmark_data = [json.loads(line) for line in f]
        if not benchmark_data:
            logging.error(f"Benchmark file '{BENCHMARK_PATH}' is empty.")
            return
    except FileNotFoundError:
        logging.error(f"Benchmark file not found at '{BENCHMARK_PATH}'.")
        return

    results = []
    if os.path.exists(CHECKPOINT_PATH):
        with open(CHECKPOINT_PATH, 'r', encoding='utf-8') as f:
            for line in f:
                results.append(json.loads(line))
    processed_qs = {res['question'] for res in results}
    logging.info(f"Found {len(processed_qs)} previously processed questions.")

    questions_to_process = [row for row in benchmark_data if row['question'] not in processed_qs]
    
    if not questions_to_process:
        logging.info("All questions already processed. Proceed to judging.")
        return

    logging.info(f"Initializing RAG pipeline systems...")
    systems = rag.initialize_systems()

    class DummySessionState:
        def __init__(self):
            self.last_retrieved_context = None

    with open(CHECKPOINT_PATH, 'a', encoding='utf-8') as f:
        for row in tqdm(questions_to_process, desc="Generating Answers"):
            question = row['question']
            session_state = DummySessionState()
            
            try:
                start_time = time.time()
                history = []
                pipeline_response = rag.run_full_pipeline(
                    user_input=question, chat_history=history, systems=systems,
                    update_callback=lambda msg: None, session_state=session_state
                )
                end_time = time.time()
                latency_ms = round((end_time - start_time) * 1000)

                answer = "".join(list(pipeline_response.get("stream", [])))
                contexts = [doc.page_content for doc in pipeline_response.get("sources", [])]
                
                ground_truth_context = row.get('ground_truth_context', [])
                if not isinstance(ground_truth_context, list):
                    ground_truth_context = []
                
                ground_truth_answer = row.get('ground_truth_answer', "") 
                
                result_item = {
                    "question": question, 
                    "answer": answer, 
                    "contexts": contexts,
                    "ground_truth_context": ground_truth_context,
                    "ground_truth_answer": ground_truth_answer,
                    "latency_ms": latency_ms
                }
                f.write(json.dumps(result_item) + '\n')

            except Exception as e:
                logging.error(f"Error processing question: '{question[:50]}...'. Error: {e}")
                continue
                
            time.sleep(CONFIG.API_SLEEP_INTERVAL)

    logging.info("Answer generation complete.")

if __name__ == "__main__":
    main()