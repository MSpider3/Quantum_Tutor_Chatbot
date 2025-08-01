# ⚛️ Quantum Tutor RAG Chatbot

This repository contains the complete source code for a sophisticated, Retrieval-Augmented Generation (RAG) chatbot designed to be a personal tutor for quantum computing. The system is built with a professional, multi-layered architecture, featuring an API-first design with a local fallback, a robust evaluation pipeline, and a user-friendly Streamlit interface.

This project is the result of an extensive development and debugging process, showcasing advanced techniques in AI engineering, from data ingestion and cleaning to state-of-the-art RAG strategies and rigorous, data-driven benchmarking.

---

## ✨ Features

*   **Advanced RAG Pipeline:**
    *   **History-Aware Retrieval:** Intelligently rewrites user questions based on conversational context to find the most relevant information.
    *   **Context Caching:** Remembers the last retrieved context for nearly instantaneous follow-up answers.
    *   **Conditional Context Distillation:** Automatically detects and summarizes overly large contexts to prevent API token limit errors.
*   **Hybrid LLM System:**
    *   **API-First Design:** Uses a powerful, fast API (Groq with Llama 3 70B) for the best user experience.
    *   **Local Fallback:** Seamlessly falls back to a local Ollama model (`llama3.1:8b`) if the API fails, ensuring high availability.
    *   **Specialist Models:** Uses smaller, faster models for simple tasks like classification and title generation.
*   **Fault-Tolerant Web Search:** If the internal knowledge base is insufficient, it falls back to a robust web search using the Tavily API, with built-in retries and error handling.
*   **Professional Evaluation Suite:**
    *   **Automated Benchmark Generation:** Includes a script to synthetically generate a high-quality benchmark dataset from source documents.
    *   **Two-Phase Evaluation:** A robust, resumable evaluation pipeline that first generates answers and then judges them for quality, latency, and correctness.
    *   **LLM-as-a-Judge:** Uses a powerful "judge" LLM to provide nuanced, 0-10 scores for metrics like Faithfulness, Context Recall, and Answer Correctness.
*   **Interactive Streamlit UI:**
    *   User authentication and multi-chat session management.
    *   Real-time answer streaming with a generation timer.
    *   Automatic conversation titling.
    *   Clickable suggested follow-up questions.
    *   A complete user feedback system.

---

## 🛠️ Tech Stack & Architecture

*   **Backend & RAG:** LangChain, Sentence Transformers, ChromaDB
*   **LLM Serving:** Groq API, Ollama (for local fallback)
*   **Web Search:** Tavily API
*   **Frontend:** Streamlit
*   **Data & Evaluation:** Pandas, Ragas (for the evaluation framework concepts), PyYAML
*   **Database:** SQLite

---

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### 1. Prerequisites

*   Python 3.11+
*   [Git](https://git-scm.com/)
*   [Ollama](https://ollama.com/) installed and running.
*   An OCR engine for image-based PDFs (Optional): [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki).

### 2. Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/MSpider3/Quantum_Tutor_Chatbot.git
    cd Quantum_Tutor_Chatbot
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Mac/Linux
    .venv\Scripts\activate   # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your secrets:**
    *   Create a file named `.env` in the project root.
    *   Copy the contents of `.env.example` into it.
    *   Add your API keys from Groq and Tavily.
    ```
    GROQ_API_KEY="gsk_YourApiKeyHere"
    TAVILY_API_KEY="tvly-YourApiKeyHere"
    ```

5.  **Pull the local LLM model:**
    ```bash
    ollama pull llama3.1:8b
    ```

### 3. How to Run

The project is divided into several independent parts: data ingestion, the chatbot application, and the evaluation suite.

#### **Step 1: Ingest Your Data**
Before running the chatbot, you must build the knowledge base.
1.  Place your `.pdf` and `.md` files into the `data_to_process` directory (it supports subfolders).
2.  Run the ingestion script from the `chatbot` directory:
    ```bash
    python chatbot/1_run_ingestion.py
    ```

#### **Step 2: Run the Streamlit Chatbot**
1.  Ensure the Ollama application is running in the background.
2.  Run the Streamlit app from the project root directory:
    ```bash
    streamlit run chatbot/app.py
    ```

#### **Step 3: (Optional) Run the Evaluation Benchmark**
This is a two-phase process.

1.  **Phase 1: Generate Answers** - This runs your chatbot over every question in the benchmark and saves the results.
    ```bash
    python chatbot/generate_answers.py
    ```
2.  **Phase 2: Judge the Answers** - This uses a powerful "judge" LLM to score the generated answers.
    ```bash
    python chatbot/judge_answers.py
    ```
    The final report will be saved in `chatbot/evaluation_results.csv`.

---

## ⚙️ Configuration

The entire project is controlled by a single, centralized configuration file: `chatbot/config.py`. This file allows you to easily tune all aspects of the system, including:
*   Model names for the primary, fallback, and summarizer LLMs.
*   Hyperparameters for the RAG retriever (`INITIAL_K`, `RERANK_K`, etc.).
*   Quality thresholds (`RERANKER_SCORE_THRESHOLD`).
*   Ingestion settings (`CHUNK_SIZE`).
