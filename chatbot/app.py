# app.py
import streamlit as st
from datetime import datetime
from langchain_core.messages import HumanMessage, AIMessage
import time
import json
# Import your existing backend modules
import database as db
import rag_pipeline as rag
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
from database import setup_database

setup_database()

st.set_page_config(page_title="Quantum Tutor", page_icon="⚛️", layout="wide")

@st.cache_resource
def get_ai_systems():
    print("--- Initializing AI systems (this will run only once) ---")
    start_time = time.time()
    systems = rag.initialize_systems()
    end_time = time.time()
    systems['load_time'] = end_time - start_time
    systems['classifier_llm'] = rag.ChatGroq(model_name="llama3-8b-8192", groq_api_key=rag.CONFIG.GROQ_API_KEY, temperature=0)
    return systems

systems = get_ai_systems()


def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "session_id" not in st.session_state:
        st.session_state.session_id = None
    if "username" not in st.session_state:
        st.session_state.username = None
    if "user_id" not in st.session_state:
        st.session_state.user_id = None
    if "last_retrieved_context" not in st.session_state:
        st.session_state.last_retrieved_context = None
    if "history" not in st.session_state:
        st.session_state.history = ChatMessageHistory()

initialize_session_state()


def timed_stream_wrapper(stream, placeholder):
    start_time = time.time()
    full_response = ""
    for chunk in stream:
        full_response += chunk
        elapsed_time = time.time() - start_time
        placeholder.markdown(f"{full_response}▌")
        placeholder.markdown(f"{full_response}\n\n--- \n*Generation time: {elapsed_time:.2f}s*")
    placeholder.markdown(f"{full_response}\n\n---\n*Generation time: {elapsed_time:.2f}s*")
    return full_response

def generate_followup_questions(question: str, answer: str, systems: dict):
    try:
        llm = systems.get("llm") 
        prompt = ChatPromptTemplate.from_template(
            """Based on the following question and answer, generate three relevant and insightful follow-up questions a curious student might ask.
            Your output MUST be a single, valid JSON object with a single key "questions" which contains a list of the three question strings.
            Do not output any other text or formatting.
            <Question>{question}</Question>
            <Answer>{answer}</Answer>
            <JSON_OUTPUT>"""
        )
        chain = prompt | llm | JsonOutputParser()
        result = chain.invoke({"question": question, "answer": answer})
        return result.get("questions", [])
    except Exception as e:
        print(f"Error generating follow-up questions: {e}")
        return []

def generate_conversation_title(systems: dict, history: ChatMessageHistory):
    llm = systems.get("classifier_llm", systems["llm"])
    # Convert LangChain messages to a simple string for the prompt
    history_str = "\n".join([f"{msg.type}: {msg.content}" for msg in history.messages])
    prompt_str = (
        "Based on the following conversation, create a concise title. "
        "The title must be 5 words or less. Do not use punctuation or quotes. "
        f"Conversation:\n{history_str}\n\nTitle:"
    )
    try:
        response = llm.invoke(prompt_str)
        clean_title = (getattr(response, "content", str(response))
                       .replace('"', '').replace("'", "").strip())
        return clean_title if clean_title else "Quantum Chat"
    except Exception as e:
        print(f"Error generating title: {e}")
        first_user_message = next((msg.content for msg in history.messages if msg.type == 'human'), "Quantum Chat")
        return " ".join(first_user_message.split()[:5])


with st.sidebar:
    st.header("⚛️ Quantum Tutor")
    if st.session_state.username:
        st.write(f"Welcome, **{st.session_state.username}**!")
        st.markdown("---")
        st.caption(f"⚡ Active Model: `{systems['llm'].model_name}`")
        st.caption(f"💾 DB Load Time: `{systems['load_time']:.2f}s`")
        st.markdown("---")
        if st.button("Logout"):
            for key in ['username', 'user_id', 'session_id', 'messages', 'last_retrieved_context']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()
    else:
        st.subheader("Login")
        username = st.text_input("Enter your username:", key="login_username", label_visibility="collapsed")
        if st.button("Login / Register"):
            if username:
                st.session_state.user_id = db.get_or_create_user(username)
                st.session_state.username = username
                st.rerun()
            else:
                st.warning("Please enter a username.")

    st.divider()

    if st.session_state.user_id:
        st.subheader("Your Chats")
        if st.button("💬 New Chat", use_container_width=True):
            st.session_state.session_id = db.create_chat_session(st.session_state.user_id)
            st.session_state.messages = []
            st.session_state.history.clear() # Clear the history object
            st.session_state.last_retrieved_context = None
            st.rerun()

        chats = db.get_user_chats(st.session_state.user_id)
        for session_id, created_at, display_title in chats:
            display_time = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S').strftime('%b %d, %Y')
            button_label = f"_{display_title}_ ({display_time})"
            if st.button(button_label, key=f"chat_{session_id}", use_container_width=True):
                st.session_state.session_id = session_id
                ui_messages, lc_history = db.load_chat_history(session_id)
                st.session_state.messages = ui_messages
                st.session_state.history = lc_history
                st.session_state.last_retrieved_context = None
                st.rerun()


st.title("Quantum Tutor Chat")

if st.session_state.user_id and not st.session_state.session_id:
    st.info("Start a new chat or select a previous one from the sidebar.")
    st.stop()

if st.session_state.session_id:
    for i, msg in enumerate(st.session_state.messages):
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            sources = msg.get("sources", [])
            if sources:
                with st.expander("View Sources"):
                    for doc_index, doc in enumerate(sources):
                        metadata = doc.get("metadata", {}) if isinstance(doc, dict) else doc.metadata
                        source_name = ( metadata.get('source_file') or metadata.get('url') or metadata.get('source') or "Unknown Source")
                        page_number = metadata.get('page_number')
                        st.markdown(f"**[{doc_index + 1}] {source_name}** {'(Page: ' + str(page_number) + ')' if page_number else ''}")

            if "suggested_questions" in msg and msg["suggested_questions"]:
                st.markdown("**Suggested Questions:**")
                cols = st.columns(len(msg["suggested_questions"]))
                for j, question in enumerate(msg["suggested_questions"]):
                    if cols[j].button(question, key=f"suggestion_{i}_{j}"):
                        st.session_state.messages.append({"role": "user", "content": question})
                        db.save_message(st.session_state.session_id, 'user', question)
                        st.rerun()

            if msg["role"] == "assistant":
                st.markdown("---")
                col1, col2, _ = st.columns([1, 1, 5])
                if col1.button("👍 Helpful", key=f"helpful_{i}"):
                    st.toast("Thank you for your feedback!", icon="😊")
                if col2.button("👎 Not Helpful", key=f"unhelpful_{i}"):
                    user_prompt = "Could not find preceding prompt."
                    if i > 0 and st.session_state.messages[i-1]["role"] == "user":
                        user_prompt = st.session_state.messages[i-1]["content"]
                    db.add_to_review_queue(st.session_state.session_id, user_prompt, msg["content"])
                    st.toast("Thank you! This chat has been flagged for review.", icon="📝")

if prompt := st.chat_input("Ask a quantum question..."):
    if not st.session_state.session_id:
        st.warning("Please start a new chat before asking a question.")
        st.stop()
    # Add to both UI messages and LangChain history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.history.add_user_message(prompt)
    db.save_message(st.session_state.session_id, 'user', prompt)
    st.rerun()

if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    user_prompt = st.session_state.messages[-1]["content"]
    with st.chat_message("assistant"):
        with st.spinner("Quantum circuits are whirring..."):
            pipeline_response = rag.run_full_pipeline(
                user_input=user_prompt,
                chat_history=st.session_state.history.messages,
                systems=systems,
                update_callback=lambda msg: None,
                session_state=st.session_state
            )
        
        response_placeholder = st.empty()
        # --- FIX: Call the new, persistent timer ---
        full_response = timed_stream_wrapper(pipeline_response.get("stream"), response_placeholder)
        sources = pipeline_response.get("sources", [])
        
        # Add AI response to both histories
        st.session_state.history.add_ai_message(full_response)
        
        with st.spinner("Generating follow-up suggestions..."):
            suggested_questions = generate_followup_questions(user_prompt, full_response, systems)
        
        ai_message = {
            "role": "assistant", "content": full_response,
            "sources": [s.model_dump() for s in sources],
            "suggested_questions": suggested_questions
        }
        st.session_state.messages.append(ai_message)
        db.save_message(st.session_state.session_id, 'ai', full_response, sources=sources)

        # --- FIX: Correct title generation logic ---
        current_chat_info = next((chat for chat in db.get_user_chats(st.session_state.user_id) if chat[0] == st.session_state.session_id), None)
        if current_chat_info and (not current_chat_info[2] or "Chat from" in current_chat_info[2]):
            if len(st.session_state.history.messages) >= 2:
                with st.spinner("Generating chat title..."):
                    title = generate_conversation_title(systems, st.session_state.history)
                    db.update_chat_session_title(st.session_state.session_id, title)
        
        st.rerun()