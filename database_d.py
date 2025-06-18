import uuid
from datetime import datetime
from sqlalchemy import (
    create_engine, Column, Integer, String, Text, DateTime, Boolean, MetaData
)
from sqlalchemy.orm import declarative_base, sessionmaker

# 🔐 Строка подключения к PostgreSQL
DATABASE_URL = (
    "postgresql://chatgpt_user:XroadChatGPTInstance@127.0.0.1:5432/chatgpt_db"
    "?options=-csearch_path=chatdata"
)

# Указываем схему chatdata
metadata = MetaData(schema="chatdata")
Base = declarative_base(metadata=metadata)

# Инициализация движка и сессий
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Модель взаимодействий
class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True)
    client_id = Column(String)
    session_id = Column(String)
    question_id = Column(String, unique=True)
    question = Column(Text)
    answer_llm1 = Column(Text)
    answer_llm2 = Column(Text)
    is_incorrect = Column(Boolean, default=False)
    suggested_answer = Column(Text, nullable=True)
    timestamp = Column(DateTime)

# Создание таблицы
def init_db():
    print("Создание таблиц в PostgreSQL...")
    Base.metadata.create_all(bind=engine)

# Сохранение взаимодействия
def save_interaction(question, answer_llm1, answer_llm2, session_id="unknown", client_id="0"):
    question_id = str(uuid.uuid4())
    timestamp = datetime.utcnow()
    with Session() as session:
        interaction = Interaction(
            client_id=client_id,
            session_id=session_id,
            question_id=question_id,
            question=question,
            answer_llm1=answer_llm1,
            answer_llm2=answer_llm2,
            timestamp=timestamp
        )
        session.add(interaction)
        session.commit()
    return question_id

# Отметить как неправильный
def mark_incorrect(question_id):
    with Session() as session:
        interaction = session.query(Interaction).filter_by(question_id=question_id).first()
        if interaction:
            interaction.is_incorrect = True
            session.commit()

# Сохранить предложенный ответ
def save_suggested_answer(question_id, text):
    with Session() as session:
        interaction = session.query(Interaction).filter_by(question_id=question_id).first()
        if interaction:
            interaction.suggested_answer = text
            session.commit()