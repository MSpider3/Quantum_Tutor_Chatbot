# config.py
import os
import torch
from dotenv import load_dotenv

load_dotenv()


class CONFIG:
    # ── API Keys ───────────────────────────────────────────────────────────────────
    # These are loaded from your .env file for security.
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    if not GROQ_API_KEY:
        raise ValueError(
            "GROQ_API_KEY not found. "
            "Please ensure you have a .env file in the project root "
            "with the line: GROQ_API_KEY=gsk_YourApiKeyHere"
        )

    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    if not TAVILY_API_KEY:
        raise ValueError(
            "TAVILY_API_KEY not found. "
            "Please ensure you have a .env file in the project root "
            "with the line: TAVILY_API_KEY=tvly-YourApiKeyHere"
        )

     # --- LLM Model Names ---
   # PRIMARY_LLM_MODEL = "openai/gpt-oss-120b"
  #  PRIMARY_LLM_MODEL = "deepseek-r1-distill-llama-70b"
  #  PRIMARY_LLM_MODEL = "qwen/qwen3-32b"
    PRIMARY_LLM_MODEL = "llama-3.3-70b-versatile"
    SUMMARIZER_LLM_MODEL = "gemma2-9b-it"
    FALLBACK_LLM_MODEL = "llama3.1:8b"
    JUDGE_LLM_MODEL = "llama-3.3-70b-versatile"

    # --- Paths ---
    DB_FILE = "tutor_database.db"
    CHROMA_PATH = "./chroma_db"
    COLLECTION_NAME = "quantum_computing_main"
    
    # --- Evaluation File Paths ---
    BENCHMARK_DATASET_PATH = "./benchmarking_data/benchmark_dataset.jsonl"
    GENERATED_ANSWERS_CHECKPOINT = "./benchmarking_data/generated_answers.jsonl"
    JUDGED_RESULTS_CHECKPOINT = "./benchmarking_data/judged_results.jsonl"
    FINAL_RESULTS_PATH = "./benchmarking_data/evaluation_results.csv"

    # --- Local Models (for ingestion & reranking) ---
    EMBEDDING_MODEL_NAME = "BAAI/bge-m3"
    RERANKER_MODEL_NAME = "BAAI/bge-reranker-large"
    
     # --- Evaluation Tuning Parameters ---
    API_SLEEP_INTERVAL = 10
    MAX_CONTEXT_CHARS = 4000
    MAX_ANSWER_CHARS = 1500
    MAX_GT_CHARS = 1500
    
    # --- RAG Tuning Hyperparameters ---
    INITIAL_K = 50
    RERANK_K = 25
    TOP_K_TO_LLM = 3
    RERANKER_SCORE_THRESHOLD = 0.4
    SAFE_CHAR_LIMIT_FOR_DISTILLATION = int(1.25 * MAX_CONTEXT_CHARS)

    # --- Ingestion Parameters ---
    CHUNK_SIZE = 1800
    CHUNK_OVERLAP = 220
    
    # --- Hardware Configuration ---
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"