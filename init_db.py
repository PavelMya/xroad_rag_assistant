from database import Base, Interaction, DATABASE_URL
from sqlalchemy import create_engine

def init_db():
    print("Создание таблиц в базе данных...")
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    print("✅ Таблицы успешно созданы.")