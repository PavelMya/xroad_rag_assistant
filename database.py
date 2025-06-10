import sqlite3
import uuid
from datetime import datetime

DB_PATH = "interactions.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id TEXT,
            session_id TEXT,
            question_id TEXT,
            question TEXT,
            answer_llm1 TEXT,
            answer_llm2 TEXT,
            is_incorrect INTEGER DEFAULT 0,
            suggested_answer TEXT DEFAULT NULL,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_interaction(question, answer_llm1, answer_llm2, session_id="unknown", client_id="0"):
    question_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO interactions (
            client_id, session_id, question_id, question,
            answer_llm1, answer_llm2, timestamp
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        client_id, session_id, question_id, question,
        answer_llm1, answer_llm2, timestamp
    ))
    conn.commit()
    conn.close()

    return question_id

def mark_incorrect(question_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE interactions SET is_incorrect = 1 WHERE question_id = ?
    """, (question_id,))
    conn.commit()
    conn.close()

def save_suggested_answer(question_id, text):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE interactions SET suggested_answer = ? WHERE question_id = ?
    """, (text, question_id))
    conn.commit()
    conn.close()
























# from sqlalchemy import create_engine, Column, Integer, String, Boolean
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import os
# from dotenv import load_dotenv


# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()


# class Interaction(Base):
#     __tablename__ = "interactions"

#     id = Column(Integer, primary_key=True, index=True)
#     client_id = Column(Integer, default=0)
#     session_id = Column(String)
#     question_id = Column(String)
#     question = Column(String)
#     answer_gpt = Column(String)
#     answer_reviewer = Column(String)
#     is_incorrect = Column(Boolean, default=False)
#     suggested_answer = Column(String, nullable=True)