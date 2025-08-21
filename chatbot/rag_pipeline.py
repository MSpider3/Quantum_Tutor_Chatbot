# rag_pipeline.py (patched)
from __future__ import annotations  # keep this first
import os
import asyncio
import time
import json
import logging
import re
import hashlib
import re  
from typing import List, Dict, Any, Tuple
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
from config import CONFIG
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableWithFallbacks
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from langchain_core.messages import AIMessage, HumanMessage
from sentence_transformers.cross_encoder import CrossEncoder
from langchain_community.retrievers import TavilySearchAPIRetriever
from langchain.chains import create_history_aware_retriever
from langchain.text_splitter import RecursiveCharacterTextSplitter

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def initialize_systems() -> Dict[str, Any]:
    logging.info("Initializing AI systems...")

    primary_llm = ChatGroq(model_name=CONFIG.PRIMARY_LLM_MODEL, groq_api_key=CONFIG.GROQ_API_KEY, temperature=0)
    summarizer_llm = ChatGroq(model_name=CONFIG.SUMMARIZER_LLM_MODEL, groq_api_key=CONFIG.GROQ_API_KEY, temperature=0)
    fallback_llm = ChatOllama(model=CONFIG.FALLBACK_LLM_MODEL, temperature=0)
    llm_with_fallback = primary_llm.with_fallbacks([fallback_llm])
    
    logging.info(f"Primary LLM: Groq ({CONFIG.PRIMARY_LLM_MODEL}). Fallback LLM: Local ({CONFIG.FALLBACK_LLM_MODEL}).")
    
    embedding_function = HuggingFaceEmbeddings(
        model_name=CONFIG.EMBEDDING_MODEL_NAME, model_kwargs={'device': CONFIG.DEVICE}
    )
    vector_store = Chroma(
        collection_name=CONFIG.COLLECTION_NAME, embedding_function=embedding_function, persist_directory=CONFIG.CHROMA_PATH
    )
    cross_encoder = CrossEncoder(CONFIG.RERANKER_MODEL_NAME, max_length=512)
    web_search_retriever = TavilySearchAPIRetriever(k=5, include_raw_content=True, tavily_api_key=CONFIG.TAVILY_API_KEY)
    
    logging.info("✅ AI Systems Initialized.")
    return {
        "llm": llm_with_fallback,
        "summarizer_llm": summarizer_llm,
        "vector_store": vector_store,
        "cross_encoder": cross_encoder,
        "web_search_retriever": web_search_retriever,
    }

def _format_context_for_llm(docs: List[Document]) -> str:
    context_str = ""
    for i, doc in enumerate(docs, 1):
        page_content = doc.page_content.replace("\n", " ").strip()
        source_file = doc.metadata.get("source_file", "Unknown")
        page_num = doc.metadata.get("page_number")
        source_info = f"{source_file} (Page: {page_num})" if page_num else source_file
        context_str += f"[{i}] Source: {source_info}\nContent: {page_content}\n\n"
    return context_str

def _clean_route_output(text: str) -> str:
    if "new_topic" in text: return "new_topic"
    if "follow_up" in text: return "follow_up"
    return "greeting"

REFUSAL_STRINGS = {
    "I'm sorry, I can only answer questions related to quantum computing based on the provided materials. The context does not contain enough information to answer your question accurately."
}

def _word_tokens(s: str) -> List[str]:
    return re.findall(r"[a-z0-9]+", s.lower())

def _content_words(s: str, min_len: int = 4) -> List[str]:
    return [w for w in _word_tokens(s) if len(w) >= min_len]

def is_refusal(ans: str) -> bool:
    norm = ans.strip().lower()
    return any(norm == s.lower() for s in REFUSAL_STRINGS)

def question_keyword_overlap_with_context(question: str, contexts: List[str] | List[Document], min_overlap: int = 1) -> bool:
    if contexts and isinstance(contexts[0], Document):
        ctx_text = " ".join(doc.page_content for doc in contexts)
    else:
        ctx_text = " ".join(contexts)
    q_kw = set(_content_words(question))
    hits = sum(1 for w in q_kw if w in ctx_text.lower())
    return hits >= min_overlap

import itertools

def harvest_evidence_sentences(raw_text: str, question: str, max_sentences: int = 4) -> List[str]:
    q_kw = {w for w in re.findall(r"[a-z0-9]+", question.lower()) if len(w) >= 4}
    candidates = re.split(r"(?<=[.!?])\s+", raw_text)
    keep = []
    seen = set()
    for s in candidates:
        s_clean = s.strip()
        if not s_clean:
            continue
        low = s_clean.lower()
        if any(kw in low for kw in q_kw):
            k = low[:200]
            if k not in seen:
                seen.add(k)
                keep.append(s_clean)
        if len(keep) >= max_sentences:
            break
    return keep

def get_router_chain(llm):
    prompt = ChatPromptTemplate.from_template(
        """You are a query classifier. Your task is to categorize the user's latest question.
Your entire response MUST be ONLY ONE of the following three strings: 'new_topic', 'follow_up', or 'greeting'.
Do NOT add any explanation, punctuation, or other text.
- 'new_topic': The user is asking about a subject for the first time or changing the subject.
- 'follow_up': The user is asking for more detail or clarification about your immediately preceding answer.
- 'greeting': A simple social reply like "hello", "thanks", or "cool".
<Chat History>{chat_history}</Chat History>
<User Question>{input}</User Question>
<CLASSIFICATION>"""
    )
    return prompt | llm | StrOutputParser() | _clean_route_output

def get_rag_chain(llm):
    strict_rag_prompt_template = """
    You are a helpful and knowledgeable quantum computing tutor. Your task is to provide answers STRICTLY AND ONLY based on the factual information in the "Context" section below.

    Follow these rules precisely:
    **Answering Guidelines:**
    - If the "Context" contains relevant information, provide a **clear, complete, and structured answer** using only that information.
    - For conceptual queries, extract explanations and properties as described in the context.
    - For comparison questions (e.g., comparing X and Y), compare them by outlining their features and any differences/similarities found in the context.
    - For questions involving Qiskit code, if the context has sufficient detail, return a single complete and correct Qiskit code block (```python ... ```).

    **Critical Formatting Rule:**
    - If you include any mathematical formulas, equations, or symbols (like |ψ⟩ or α), you **MUST** enclose them in dollar signs for proper rendering (e.g., $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$).

    **Strict Disclaimer Rule:**
    - **IF** the "Context" does NOT contain information that directly relates to the Question, you **MUST** respond with the **EXACT AND ONLY** following disclaimer: "I'm sorry, I can only answer questions related to quantum computing based on the provided materials. The context does not contain enough information to answer your question accurately."
    - **UNDER NO CIRCUMSTANCES** should you use your general knowledge.
    
    **NO-REFUSAL RULE**: If the Context contains ANY sentence that mentions at least one keyword from the Question (≥4 letters), you MUST attempt an answer strictly from the Context. Do NOT output the disclaimer in this case. If information is partial, answer with what is present and explicitly note the limits.

    If the Context does NOT contain enough information to answer the Question, you MUST respond with the EXACT AND ONLY following disclaimer:
    "I'm sorry, I can only answer questions related to quantum computing based on the provided materials. The context does not contain enough information to answer your question accurately."

    Context:
    {context}
    Question: {question}
    Answer:
    """

    prompt = ChatPromptTemplate.from_messages([
        ("system", strict_rag_prompt_template),
        ("placeholder", "{chat_history}"),
        ("human", "{question}")
    ])
    return prompt | llm | StrOutputParser()

def get_rag_chain_force_answer(llm):
    force_template = """
    You are a helpful and knowledgeable quantum computing tutor. Provide an answer ONLY from the Context.

    **DO NOT REFUSE**: If any question keyword appears in the Context, you must answer from the Context. Do not apologize.

    Context:
    {context}
    Question: {question}
    Answer:
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", force_template),
        ("placeholder", "{chat_history}"),
        ("human", "{question}")
    ])
    return prompt | llm | StrOutputParser()

def distill_context_with_forced_keep(summarizer_llm, documents: List[Document], question: str) -> str:
    q_kw = {w for w in _content_words(question, min_len=4)}
    raw_text = " ".join(doc.page_content for doc in documents)

    forced_sentences = []
    for s in re.split(r"(?<=[.!?])\s+", raw_text):
        if any(kw in s.lower() for kw in q_kw):
            forced_sentences.append(s.strip())

    distillation_prompt = ChatPromptTemplate.from_template(
        "You are a helpful assistant. Condense the following context into a concise summary that is highly relevant "
        "to the user's question. Retain all key facts and numbers. Do not answer the question, just summarize the context.\n\n"
        "Question: {question}\n\nContext: {context}\n\nSummary:"
    )
    distill_chain = distillation_prompt | summarizer_llm | StrOutputParser()

    CHUNK_SIZE = 3500 
    distilled_summary = ""

    if len(raw_text) > CHUNK_SIZE:
        logging.info(f"Context is large ({len(raw_text)} chars), distilling in chunks.")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=200)
        chunks = text_splitter.split_text(raw_text)

        summaries = []
        for i, chunk in enumerate(chunks):
            logging.info(f"Summarizing chunk {i+1}/{len(chunks)} ({len(chunk)} chars)...")
            summary = distill_chain.invoke({"question": question, "context": chunk})
            summaries.append(summary)

        distilled_summary = "\n".join(summaries)
    else:
        logging.info("Context is small enough, distilling in a single pass.")
        distilled_summary = distill_chain.invoke({"question": question, "context": raw_text})

    combined_list = list(dict.fromkeys(forced_sentences + distilled_summary.splitlines()))
    combined_text = "\n".join(combined_list)

    return combined_text[: CONFIG.SAFE_CHAR_LIMIT_FOR_DISTILLATION]


def get_contextual_rag_chain(llm):
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a helpful quantum computing tutor. The user is asking a follow-up question. Use the PREVIOUSLY PROVIDED CONTEXT below to answer their NEW QUESTION. Follow all the same rules."""),
        ("placeholder", "{chat_history}"),
        ("human", """PREVIOUSLY PROVIDED CONTEXT:\n{context}\n\nBased *only* on the context above, answer the user's NEW QUESTION: {question}""")
    ])
    return prompt | llm | StrOutputParser()


def get_web_chain(llm):
    prompt = ChatPromptTemplate.from_template(
        """You are a Factual Reporting Bot. Provide a concise answer to the 'User Question' by synthesizing the numbered 'Web Search Results'.
- You MUST NOT use any internal knowledge.
- If the search results do not contain enough information, state that you could not find a direct answer.
- If only part of the question can be answered, answer that part and state what is missing.
Web Search Results:\n{context}\n\nUser Question: {input}"""
    )
    return prompt | llm | StrOutputParser()


def get_conversational_rag_chain(llm):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Be friendly and direct."),
        ("placeholder", "{chat_history}"),
        ("human", "{input}")
    ])
    return prompt | llm | StrOutputParser()


def get_question_rewriter_chain(llm):
    """Creates a chain that rewrites a follow-up question into a standalone question."""
    _template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question, in its original language.
    Analyze the chat history to see if the follow up question is a direct continuation of the last answer (e.g., asking to explain the previous response).
    - If it is a direct continuation, incorporate the key topic from the last answer into the standalone question.
    - If it is a completely new topic, simply rephrase the follow up question.

    Chat History:
    {chat_history}
    Follow Up Input: {input}
    Standalone question:"""
    prompt = ChatPromptTemplate.from_template(_template)
    return prompt | llm | StrOutputParser()

# --- Core Retrieval Logic ---
def retrieve_and_rerank(user_input: str, chat_history: list, systems: Dict, update_callback) -> Tuple[List[Document], str]:
    vector_store = systems["vector_store"]
    cross_encoder = systems["cross_encoder"]
    llm = systems["llm"]

    update_callback("Analyzing history and searching documents...")

    # Build a history-aware retriever (same as before)
    from langchain_core.prompts import ChatPromptTemplate
    from langchain.chains import create_history_aware_retriever

    contextualize_q_prompt = ChatPromptTemplate.from_messages([
        ("system", """Given a chat history and the latest user question which might reference context in the chat history, formulate a standalone question which can be understood without the chat history. Do NOT answer the question, just reformulate it if needed and otherwise return it as is."""),
        ("placeholder", "{chat_history}"),
        ("human", "{input}")
    ])

    history_aware_retriever = create_history_aware_retriever(
        llm, vector_store.as_retriever(search_kwargs={"k": CONFIG.INITIAL_K}), contextualize_q_prompt
    )

    initial_docs: List[Document] = history_aware_retriever.invoke({"chat_history": chat_history, "input": user_input})

    if not initial_docs:
        logging.warning("History-aware retrieval returned no documents.")
        return [], "FAILURE"

    update_callback(f"Reranking {len(initial_docs)} results...")

    def _fingerprint(doc: Document):
        meta_key = (
            doc.metadata.get("source_file"),
            doc.metadata.get("page_number"),
            doc.metadata.get("chunk_id"), 
        )
        if any(meta_key):
            return meta_key
        norm = re.sub(r"\s+", " ", doc.page_content.strip().lower())
        return hashlib.md5(norm.encode("utf-8")).hexdigest()

    seen = set()
    dedup_docs: List[Document] = []
    for d in initial_docs:
        fp = _fingerprint(d)
        if fp in seen:
            continue
        seen.add(fp)
        dedup_docs.append(d)

    pairs = [[user_input, doc.page_content] for doc in dedup_docs]
    scores = cross_encoder.predict(pairs, show_progress_bar=False)
    scored_docs = sorted(zip(scores, dedup_docs), key=lambda x: x[0], reverse=True)

    if not scored_docs or scored_docs[0][0] < CONFIG.RERANKER_SCORE_THRESHOLD:
        logging.warning(
            f"No documents met the reranker threshold of {CONFIG.RERANKER_SCORE_THRESHOLD}."
        )
        return [], "FAILURE"

    scored_docs = scored_docs[: CONFIG.RERANK_K]

    def _short_hash(text: str) -> str:
        norm = re.sub(r"\s+", " ", text).strip().lower()
        return hashlib.md5(norm.encode()).hexdigest()[:8]

    top5 = [f"{s:.4f}" for s, _ in scored_docs[:5]]
    logging.info(f"Top 5 reranker scores: {top5}")
    for i, (s, d) in enumerate(scored_docs[:5], 1):
        h = _short_hash(d.page_content)
        src = d.metadata.get("source_file")
        pno = d.metadata.get("page_number")
        logging.debug(f"Top {i}: {s:.6f}  hash={h}  src={src}  p={pno}")

    def _jaccard_sim(a: str, b: str) -> float:
        A = set(re.findall(r"[a-z0-9]+", a.lower()))
        B = set(re.findall(r"[a-z0-9]+", b.lower()))
        if not A or not B:
            return 0.0
        return len(A & B) / len(A | B)

    diverse: List[Document] = []
    for s, d in scored_docs:
        if all(_jaccard_sim(d.page_content, kept.page_content) < 0.90 for kept in diverse):
            diverse.append(d)
        if len(diverse) >= CONFIG.TOP_K_TO_LLM:
            break

    if len(diverse) < CONFIG.TOP_K_TO_LLM:
        for s, d in scored_docs:
            if d not in diverse:
                diverse.append(d)
            if len(diverse) >= CONFIG.TOP_K_TO_LLM:
                break

    high_quality_docs = diverse
    return high_quality_docs, "SUCCESS"



def retry_force_answer(user_input: str, chat_history: List, systems: Dict, documents: List[Document]) -> Dict[str, Any]:
    llm = systems["llm"]
    context = _format_context_for_llm(documents)
    chain = get_rag_chain_force_answer(llm)
    answer_text = chain.invoke({"input": user_input ,"question": user_input, "chat_history": chat_history, "context": context})
    return {"answer": answer_text, "sources": documents}


def run_full_pipeline(user_input: str, chat_history: List, systems: Dict, update_callback, session_state) -> Dict[str, Any]:
    llm = systems["llm"]
    summarizer_llm = systems["summarizer_llm"]
    router_chain = get_router_chain(llm)
    
    route = router_chain.invoke({"input": user_input, "chat_history": chat_history})
    logging.info(f"Router classified question as: '{route}'")

    if route == "new_topic" or (route == "follow_up" and not session_state.last_retrieved_context):
        if route == "follow_up":
            logging.warning("Router classified as follow-up, but no context was cached.")
        
        documents, status = retrieve_and_rerank(user_input, chat_history, systems, update_callback)
        
        if status == "SUCCESS":
            session_state.last_retrieved_context = documents
            
            total_context_chars = sum(len(doc.page_content) for doc in documents)
            if total_context_chars > CONFIG.SAFE_CHAR_LIMIT_FOR_DISTILLATION:
                logging.warning(f"Context exceeds safe limit. Distilling...")
                update_callback("Condensing large context...")
                distilled_text = distill_context_with_forced_keep(summarizer_llm, documents, user_input)
                summary_or_raw = distilled_text
            else:
                summary_or_raw = _format_context_for_llm(documents)

            raw_blob = " ".join(doc.page_content for doc in documents)
            evidence = harvest_evidence_sentences(raw_blob, user_input, max_sentences=4)
            evidence_block = "" 
            if evidence:
                trimmed = []
                for s in evidence[:6]: 
                    s = s.strip()
                    if len(s) > 180:
                        s = s[:180] + "…"
                    trimmed.append(s)
                bullets = "\n".join(f"- {s}" for s in trimmed)
                evidence_block = f"Evidence (verbatim quotes):\n{bullets}\n\n"

            final_context = (f"{evidence_block}{summary_or_raw}")[: CONFIG.MAX_CONTEXT_CHARS] 
            rag_chain = get_rag_chain(llm)
            answer_stream = rag_chain.stream({
                "question": user_input,
                "chat_history": chat_history,
                "context": final_context
            })
            return {"stream": answer_stream, "sources": documents, "final_context": final_context} 
        else:
            session_state.last_retrieved_context = None
            update_callback("Local search failed. Searching the web...")
            web_search_retriever = systems["web_search_retriever"]
            try:
                web_docs = web_search_retriever.invoke(user_input)
                for d in web_docs:
                    meta = d.metadata
                    meta.setdefault("source_file", meta.get("url") or meta.get("source") or "Unknown")
            except Exception as e:
                logging.error(f"Tavily web search failed: {e}")
                web_docs = []

            if not web_docs:
                def failure_stream():
                    yield "I couldn't find an answer in my documents or on the web."
                return {"stream": failure_stream(), "sources": [], "final_context": ""}

            context = _format_context_for_llm(web_docs)
            final_context = context  
            web_chain = get_web_chain(llm)
            answer_stream = web_chain.stream({"input": user_input, "context": context})
            return {"stream": answer_stream, "sources": web_docs, "final_context": final_context}
    
    elif route == "follow_up":
        update_callback("Understanding follow-up question...")
        rewriter_chain = get_question_rewriter_chain(llm)
        # The rewriter chain expects 'input' for the user's latest message
        standalone_question = rewriter_chain.invoke({"chat_history": chat_history, "input": user_input})
        logging.info(f"Rewritten question for context: '{standalone_question}'")
        
        update_callback("Answering follow-up using previous context...")
        documents = session_state.last_retrieved_context
        context = _format_context_for_llm(documents)
        contextual_chain = get_contextual_rag_chain(llm)
        # The contextual chain now expects 'question'
        answer_stream = contextual_chain.stream({"question": standalone_question, "chat_history": chat_history, "context": context})
        return {"stream": answer_stream, "sources": documents}
    
    else: # Handles "greeting"
        session_state.last_retrieved_context = None 
        update_callback("Generating response...")
        convo_chain = get_conversational_rag_chain(llm)
        # The conversational chain expects 'input'
        answer_stream = convo_chain.stream({"input": user_input, "chat_history": chat_history})
        return {"stream": answer_stream, "sources": []}