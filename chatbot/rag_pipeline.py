# rag_pipeline.py
import os
import asyncio
import time
import json
import logging
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

# --- Professional-Grade Setup ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# --- System Initialization ---
def initialize_systems() -> Dict[str, Any]:
    """Loads all models and components based on the central CONFIG object."""
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

# --- Helper Functions ---
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
    """Cleans the router's output to extract only the keyword."""
    if "new_topic" in text: return "new_topic"
    if "follow_up" in text: return "follow_up"
    return "greeting"

# --- Chain Definitions ---
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
    You are a helpful and knowledgeable quantum computing tutor.
    Your primary goal is to answer questions **EXCLUSIVELY** based on the factual information provided in the "Context" section below.

    **Answering Guidelines:**
    - If the "Context" contains relevant information, provide a **clear, complete, and structured answer** using only that information.
    - For conceptual or definitional queries, extract explanations, properties, or terms **as described in the context**.
    - For **comparison questions** (e.g., comparing X and Y):
        - If the context includes both entities, compare them by outlining their individual features and any differences/similarities.
        - Do not fabricate a comparison if only one of the items is described.

    **When the Question involves construction, implementation, or Qiskit code:**
    - Look for any **descriptions, components, or full examples** in the context related to the quantum algorithm or state requested.
    - If the context provides sufficient detail, return a **single complete Qiskit code block** (```python ... ```) that:
        - Uses appropriate imports and standard syntax.
        - Builds the requested circuit accurately.
    - If only partial details are present, compose a **complete and correct code block** based on those elements.
    
    **STRICT DISCLAIMER RULE:**
    - **IF** the "Context" does NOT contain *any* information that directly or indirectly relates to the Question, you **MUST** respond with the **EXACT AND ONLY** following disclaimer.
    "I'm sorry, I can only answer questions related to quantum computing based on the provided materials. The context does not contain enough information to answer your question accurately."
    - **UNDER NO CIRCUMSTANCES** should you use your general knowledge if the provided "Context" is insufficient.

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

def get_contextual_rag_chain(llm):
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a helpful quantum computing tutor. The user is asking a follow-up question. Use the PREVIOUSLY PROVIDED CONTEXT below to answer their NEW QUESTION. Follow all the same rules for citation and asking a final question."""),
        ("placeholder", "{chat_history}"),
        ("human", """PREVIOUSLY PROVIDED CONTEXT:\n{context}\n\nBased *only* on the context above, answer the user's NEW QUESTION: {input}""")
    ])
    return prompt | llm | StrOutputParser()

def get_web_chain(llm):
    prompt = ChatPromptTemplate.from_template(
        """You are a Factual Reporting Bot. Your task is to provide a concise answer to the 'User Question' by synthesizing the numbered 'Web Search Results'.
- You MUST NOT use any of your own internal knowledge.
- If the search results do not contain enough information, simply state that you could not find a direct answer on the web.
- If you can only answer part of the question, answer that part and state which part you could not find information for.
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
    prompt = ChatPromptTemplate.from_messages([
        ("system", """Given a chat history and the latest user question which might reference context in the chat history, formulate a standalone question which can be understood without the chat history. Do NOT answer the question, just reformulate it if needed and otherwise return it as is."""),
        ("placeholder", "{chat_history}"),
        ("human", "{input}")
    ])
    return prompt | llm | StrOutputParser()

# --- Core Retrieval Logic ---
def retrieve_and_rerank(user_input: str, chat_history: list, systems: Dict, update_callback) -> Tuple[List[Document], str]:
    vector_store = systems["vector_store"]
    cross_encoder = systems["cross_encoder"]
    llm = systems["llm"]
    update_callback("Analyzing history and searching documents...")
    
    contextualize_q_prompt = ChatPromptTemplate.from_messages([
        ("system", """Given a chat history and the latest user question which might reference context in the chat history, formulate a standalone question which can be understood without the chat history. Do NOT answer the question, just reformulate it if needed and otherwise return it as is."""),
        ("placeholder", "{chat_history}"),
        ("human", "{input}")
    ])
    history_aware_retriever = create_history_aware_retriever(
        llm, vector_store.as_retriever(search_kwargs={"k": CONFIG.INITIAL_K}), contextualize_q_prompt
    )
    initial_docs = history_aware_retriever.invoke({"chat_history": chat_history, "input": user_input})

    if not initial_docs:
        logging.warning("History-aware retrieval returned no documents.")
        return [], "FAILURE"

    update_callback(f"Reranking {len(initial_docs)} results...")
    pairs = [[user_input, doc.page_content] for doc in initial_docs]
    scores = cross_encoder.predict(pairs, show_progress_bar=False)
    scored_docs = sorted(zip(scores, initial_docs), key=lambda x: x[0], reverse=True)
    logging.info(f"Top 5 reranker scores: {[f'{s:.4f}' for s, _ in scored_docs[:5]]}")

    if not scored_docs or scored_docs[0][0] < CONFIG.RERANKER_SCORE_THRESHOLD:
        logging.warning(f"No documents met the reranker threshold of {CONFIG.RERANKER_SCORE_THRESHOLD}.")
        return [], "FAILURE"

    high_quality_docs = [doc for score, doc in scored_docs if score >= CONFIG.RERANKER_SCORE_THRESHOLD]
    return high_quality_docs[:CONFIG.TOP_K_TO_LLM], "SUCCESS"

# --- Master Pipeline (Asynchronous Version) ---
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
                distillation_prompt = ChatPromptTemplate.from_template("...")
                distill_chain = distillation_prompt | summarizer_llm | StrOutputParser()
                full_context_str = "\n---\n".join([doc.page_content for doc in documents])
                distilled_text = distill_chain.invoke({"question": user_input, "context": full_context_str})
                final_context_docs = [Document(page_content=distilled_text, metadata={"source_file": "Summarized Sources"})]
            else:
                final_context_docs = documents

            context = _format_context_for_llm(final_context_docs)
            rag_chain = get_rag_chain(llm)
            answer_stream = rag_chain.stream({
                "question": user_input,
                "chat_history": chat_history, 
                "context": context
            })
            return {"stream": answer_stream, "sources": documents}
        else:
            session_state.last_retrieved_context = None
            update_callback("Local search failed. Searching the web...")
            web_search_retriever = systems["web_search_retriever"]
            try:
                web_docs = web_search_retriever.invoke(user_input)
                for d in web_docs:
                    meta=d.metadata
                    meta.setdefault("source_file", meta.get("url") or meta.get("source") or "Unknown")
            except Exception as e:
                logging.error(f"Tavily web search failed: {e}")
                web_docs = []

            if not web_docs:
                def failure_stream(): yield "I couldn't find an answer in my documents or on the web."
                return {"stream": failure_stream(), "sources": []}

            # 3. The manual list comprehension is no longer needed
            context = _format_context_for_llm(web_docs)
            web_chain = get_web_chain(llm)
            answer_stream = web_chain.stream({"input": user_input, "context": context})
            return {"stream": answer_stream, "sources": web_docs}
    
    elif route == "follow_up":
        update_callback("Understanding follow-up question...")
        rewriter_chain = get_question_rewriter_chain(llm)
        standalone_question = rewriter_chain.ainvoke({"chat_history": chat_history, "input": user_input})
        logging.info(f"Rewritten question for context: '{standalone_question}'")
        
        update_callback("Answering follow-up using previous context...")
        documents = session_state.last_retrieved_context
        context = _format_context_for_llm(documents)
        contextual_chain = get_contextual_rag_chain(llm)
        answer_stream = contextual_chain.stream({"question": standalone_question, "chat_history": chat_history, "context": context})
        return {"stream": answer_stream, "sources": documents}
    
    else: # Handles "greeting"
        session_state.last_retrieved_context = None 
        update_callback("Generating response...")
        convo_chain = get_conversational_rag_chain(llm)
        answer_stream = convo_chain.stream({"input": user_input, "chat_history": chat_history})
        return {"stream": answer_stream, "sources": []}
