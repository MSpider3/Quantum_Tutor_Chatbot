# database.py
import sqlite3
import json
from contextlib import contextmanager
from datetime import datetime
from config import CONFIG
from langchain_core.messages import HumanMessage, AIMessage
from langchain_community.chat_message_histories import ChatMessageHistory

# --- CHANGE 1: Create a context manager for database connections ---
# This decorator creates a 'with' block that handles opening, committing,
# rolling back, and closing the connection automatically and safely.
@contextmanager
def get_db_connection():
    """
    Provides a transactional database connection as a context manager.
    It ensures the connection is always closed and transactions are handled.
    """
    conn = sqlite3.connect(CONFIG.DB_FILE, check_same_thread=False)
    try:
        yield conn  # The 'conn' object is provided to the 'with' block
        conn.commit()  # If the block finishes without error, commit changes
    except Exception as e:
        conn.rollback()  # If an error occurs, undo all changes in the block
        print(f"Database error: {e}")
        raise e
    finally:
        conn.close()  # This always runs, ensuring the connection is closed

def setup_database():
    """Sets up the initial database schema using the new robust connection."""
    # The 'with' statement makes this function much cleaner and safer.
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS chat_sessions (session_id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, session_name TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY(user_id) REFERENCES users(user_id))''')

        # --- CHANGE 2: Modify the chat_messages table schema ---
        # We add a 'sources' column to store structured source data separately from the message.
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chat_messages (
                message_id INTEGER PRIMARY KEY,
                session_id INTEGER NOT NULL,
                sender TEXT NOT NULL,
                message TEXT NOT NULL,
                sources TEXT,  -- Storing sources as a structured JSON string
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(session_id) REFERENCES chat_sessions(session_id)
            )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS review_queue (review_id INTEGER PRIMARY KEY, session_id INTEGER NOT NULL, user_question TEXT NOT NULL, bot_answer TEXT NOT NULL, status TEXT DEFAULT 'pending', created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY(session_id) REFERENCES chat_sessions(session_id))''')

# --- All subsequent functions are now cleaner and safer ---

def update_chat_session_title(session_id, new_title):
    """Updates the title of a specific chat session."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE chat_sessions SET session_name = ? WHERE session_id = ?", (new_title, session_id))

def get_or_create_user(username):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        if user:
            return user[0]
        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        return cursor.lastrowid

def get_user_chats(user_id: str):
    """Return recent chat sessions plus a display title for the sidebar."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT
                session_id,
                created_at,
                COALESCE(
                    session_name,                           -- preferred: saved title
                    (
                        SELECT message                      -- fallback: 1st user prompt
                        FROM   chat_messages
                        WHERE  session_id = cs.session_id
                          AND  sender = 'user'
                        ORDER  BY timestamp
                        LIMIT  1
                    )
                ) AS display_title
            FROM   chat_sessions cs
            WHERE  user_id = ?
            ORDER  BY created_at DESC
            """,
            (user_id,),
        )
        return cursor.fetchall()

def load_chat_history(session_id):
    """
    Loads chat history for both the UI and the LangChain history object.
    Returns a tuple: (list_of_dicts_for_ui, ChatMessageHistory_object).
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT sender, message, sources FROM chat_messages WHERE session_id = ? ORDER BY timestamp ASC", (session_id,))
        messages = cursor.fetchall()

    ui_history = []
    lc_history = ChatMessageHistory()
    for sender, msg, sources_json in messages:
        if sender == 'user':
            ui_history.append({"role": "user", "content": msg})
            lc_history.add_user_message(msg)
        else:
            sources = json.loads(sources_json) if sources_json else []
            ui_history.append({"role": "assistant", "content": msg, "sources": sources})
            lc_history.add_ai_message(msg)
            
    return ui_history, lc_history

def create_chat_session(user_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO chat_sessions (user_id, session_name) VALUES (?, ?)", (user_id, f"Chat from {datetime.now().strftime('%Y-%m-%d %H:%M')}"))
        return cursor.lastrowid

# --- CHANGE 3: Update save_message to handle sources ---
def save_message(session_id, sender, message, sources: list = None):
    """Saves a message to the database, with optional structured sources."""
    # Convert the list of source documents/dictionaries into a JSON string for storage.
    sources_json = json.dumps([s.dict() for s in sources]) if sources else None
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO chat_messages (session_id, sender, message, sources) VALUES (?, ?, ?, ?)",
            (session_id, sender, message, sources_json)
        )

def add_to_review_queue(session_id, question, answer):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO review_queue (session_id, user_question, bot_answer) VALUES (?, ?, ?)", (session_id, question, answer))
    print("\n[Admin: Thank you for your feedback. This interaction has been flagged for review.]")