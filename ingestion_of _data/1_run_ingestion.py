import os
import json
import logging
import hashlib
import time
import threading
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict, Any, Optional

import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

from langchain.docstore.document import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from tqdm import tqdm

TESSERACT_CMD_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD_PATH

# --- CONFIGURATION ---
class CONFIG:
    """Configuration class for the ingestion pipeline."""
    DATA_PATH = "./data_to_process/"
    CHROMA_PATH = "./chroma_db"
    CACHE_FILE = "./ingestion_cache.json"
    LOG_FILE = "./ingestion.log"
    COLLECTION_NAME = "quantum_computing_main"

    EMBEDDING_MODEL_NAME = 'BAAI/bge-m3'
    EMBEDDING_BATCH_SIZE = 6 # Batches for the single store_worker

    CHUNK_SIZE = 512
    CHUNK_OVERLAP = 100
    MARKDOWN_HEADERS_TO_SPLIT_ON = [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")]
    
    # --- FIX: Define separate workers for CPU-bound and GPU-bound tasks ---
    # Use many workers for parsing files (CPU-bound)
    CPU_WORKERS = (os.cpu_count() or 1) - 1 or 1
    # Use only ONE worker for embedding/storage (GPU-bound)
    GPU_WORKERS = 1
    QUEUE_MAX_SIZE = CPU_WORKERS * 2

# (Script state and basic logging/caching functions are fine)
cache_lock = threading.Lock()
processed_files_count = 0
total_vectors_ingested = 0

def setup_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] [%(threadName)s] %(message)s", handlers=[logging.FileHandler(CONFIG.LOG_FILE, mode='w'), logging.StreamHandler()])
    logging.getLogger('pylatexenc').setLevel(logging.WARNING)

def calculate_file_hash(filepath: str) -> Optional[str]:
    # ... no changes ...
    hasher = hashlib.md5()
    try:
        with open(filepath, 'rb') as f: hasher.update(f.read())
        return hasher.hexdigest()
    except IOError as e:
        logging.error(f"Could not read file for hashing: {filepath} - {e}"); return None

def load_cache() -> Dict[str, str]:
    # ... no changes ...
    if os.path.exists(CONFIG.CACHE_FILE):
        try:
            with open(CONFIG.CACHE_FILE, 'r') as f: return json.load(f)
        except json.JSONDecodeError:
            logging.warning("Cache file is corrupted. Starting with an empty cache."); return {}
    return {}

def save_cache(cache: Dict[str, str]):
    # ... no changes ...
    with open(CONFIG.CACHE_FILE, 'w') as f: json.dump(cache, f, indent=4)

# --- FIX: Removed the normalize_text function entirely ---

# --- DOCUMENT PROCESSING ---
def process_pdf(filepath: str) -> List[Document]:
    """
    Processes a PDF, using OCR as a fallback for pages that are images.
    """
    filename = os.path.basename(filepath)
    chunks = []
    try:
        doc = fitz.open(filepath)
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=CONFIG.CHUNK_SIZE, chunk_overlap=CONFIG.CHUNK_OVERLAP)
        
        for page_num, page in enumerate(doc, start=1):
            # First, try to get the text directly.
            raw_text = page.get_text().strip()
            
            # --- FIX: If no text is found, use OCR as a fallback ---
            if not raw_text:
                logging.info(f"Page {page_num} in {filename} has no text layer. Attempting OCR...")
                try:
                    # Render the page as a high-resolution image
                    pix = page.get_pixmap(dpi=300)
                    img_bytes = pix.tobytes("png")
                    image = Image.open(io.BytesIO(img_bytes))
                    
                    # Use pytesseract to extract text from the image
                    raw_text = pytesseract.image_to_string(image).strip()
                    
                    if raw_text:
                        logging.info(f"Successfully extracted text from page {page_num} using OCR.")
                    else:
                        logging.warning(f"OCR for page {page_num} in {filename} yielded no text.")
                        continue # Skip this page if OCR also fails
                except Exception as ocr_error:
                    logging.error(f"OCR failed for page {page_num} in {filename}. Error: {ocr_error}")
                    continue # Skip this page on OCR error

            # The rest of the chunking process is the same.
            page_doc = Document(page_content=raw_text, metadata={"source_file": filename, "page_number": page_num})
            page_chunks = text_splitter.split_documents([page_doc])
            chunks.extend(page_chunks)
        
        logging.info(f"Extracted {len(chunks)} chunks from {filename} (including OCR).")
        return chunks
    except Exception as e:
        logging.error(f"Failed to process PDF {filename}: {e}", exc_info=True)
        return []

def process_markdown(filepath: str) -> List[Document]:
    """Processes a Markdown file, preserving raw text without LaTeX normalization."""
    filename = os.path.basename(filepath)
    try:
        with open(filepath, 'r', encoding='utf-8') as f: content = f.read()
        
        markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=CONFIG.MARKDOWN_HEADERS_TO_SPLIT_ON, return_each_line=False)
        chunks = markdown_splitter.split_text(content)
        
        # Add source file metadata to all chunks
        for chunk in chunks: chunk.metadata["source_file"] = filename
        
        logging.info(f"Extracted {len(chunks)} chunks from {filename}.")
        return chunks
    except Exception as e:
        logging.error(f"Failed to process Markdown {filename}: {e}", exc_info=True); return []

def process_document(filepath: str) -> List[Document]:
    if filepath.lower().endswith(".pdf"): return process_pdf(filepath)
    elif filepath.lower().endswith(".md"): return process_markdown(filepath)
    else:
        logging.warning(f"Unsupported file type skipped: {os.path.basename(filepath)}"); return []

# --- CONCURRENT WORKERS ---
def parse_worker(file_queue: Queue, chunk_queue: Queue):
    """CPU-bound worker that parses a file and puts its chunks on the chunk_queue."""
    while True:
        filepath = file_queue.get()
        if filepath is None: break
        try:
            chunks = process_document(filepath)
            if chunks: chunk_queue.put((filepath, chunks))
        except Exception as e:
            logging.error(f"Error during parsing of {os.path.basename(filepath)}: {e}", exc_info=True)
        finally:
            file_queue.task_done()

def store_worker(chunk_queue: Queue, vector_store: Chroma, cache: Dict[str, str], progress_bar: tqdm):
    """GPU-bound worker that ingests chunks into ChromaDB in managed batches."""
    global processed_files_count, total_vectors_ingested
    while True:
        item = chunk_queue.get()
        if item is None: break
        
        filepath, chunks = item
        filename = os.path.basename(filepath)
        
        try:
            num_chunks = len(chunks)
            for i in range(0, num_chunks, CONFIG.EMBEDDING_BATCH_SIZE):
                batch = chunks[i:i + CONFIG.EMBEDDING_BATCH_SIZE]
                if batch: vector_store.add_documents(documents=batch)
            
            file_hash = calculate_file_hash(filepath)
            with cache_lock:
                if file_hash: cache[filepath] = file_hash
                processed_files_count += 1
                total_vectors_ingested += num_chunks
                
            logging.info(f"Successfully ingested {num_chunks} vectors from {filename}.")
        except Exception as e:
            logging.error(f"CRITICAL FAILURE ingesting chunks from {filename}: {e}", exc_info=True)
        finally:
            chunk_queue.task_done()
            progress_bar.update(1)

# --- MAIN EXECUTION ---
def main():
    """Main function to orchestrate the entire ingestion pipeline."""
    setup_logging()
    start_time = time.time()
    
    cache = load_cache()
    logging.info(f"Loaded {len(cache)} files from cache.")
    
    all_source_files = [os.path.join(p, f) for p, _, fs in os.walk(CONFIG.DATA_PATH) for f in fs if f.lower().endswith(('.pdf', '.md'))]
    files_to_process = [f for f in all_source_files if cache.get(f) != calculate_file_hash(f)]

    if not files_to_process:
        logging.info("All documents are up-to-date. Exiting."); return

    logging.info(f"Found {len(files_to_process)} new or modified files to process.")
    
    file_queue = Queue()
    chunk_queue = Queue(maxsize=CONFIG.QUEUE_MAX_SIZE)
    for filepath in files_to_process: file_queue.put(filepath)

    logging.info("Initializing embedding model...")
    device = 'cuda' if __import__('torch').cuda.is_available() else 'cpu'
    embedding_function = HuggingFaceEmbeddings(
        model_name=CONFIG.EMBEDDING_MODEL_NAME, model_kwargs={'device': device}, encode_kwargs={'normalize_embeddings': True}
    )
    logging.info(f"Embedding model will use device: {device.upper()}")

    logging.info("Initializing Chroma vector store...")
    vector_store = Chroma(collection_name=CONFIG.COLLECTION_NAME, embedding_function=embedding_function, persist_directory=CONFIG.CHROMA_PATH)

    logging.info(f"Starting ingestion with {CONFIG.CPU_WORKERS} parsing workers and {CONFIG.GPU_WORKERS} storage worker...")
    
    with tqdm(total=len(files_to_process), desc="Ingesting Files", unit="file") as progress_bar:
        with ThreadPoolExecutor(max_workers=CONFIG.CPU_WORKERS + CONFIG.GPU_WORKERS, thread_name_prefix='Worker') as executor:
            # --- FIX: Dedicate most workers to parsing and only one to storage ---
            parser_threads = [executor.submit(parse_worker, file_queue, chunk_queue) for _ in range(CONFIG.CPU_WORKERS)]
            storage_thread = executor.submit(store_worker, chunk_queue, vector_store, cache, progress_bar)

            file_queue.join()
            for _ in parser_threads: file_queue.put(None)

            # Wait for parsers to finish and signal storage thread to finish
            for t in parser_threads: t.result()
            chunk_queue.put(None)
            storage_thread.result()

    logging.info("Saving updated cache...")
    save_cache(cache)
    
    logging.info("--- INGESTION COMPLETE ---")
    logging.info(f"Total time taken: {time.time() - start_time:.2f} seconds")
    logging.info(f"Total files processed in this run: {processed_files_count}")
    logging.info(f"Total vectors ingested in this run: {total_vectors_ingested}")

if __name__ == "__main__":
    main()