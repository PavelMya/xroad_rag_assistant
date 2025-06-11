import csv
from sqlalchemy import create_engine, text

# Подключение к PostgreSQL — подставь свой актуальный URL, если нужно
DATABASE_URL = (
    "postgresql://chatgpt_user:XroadChatGPTInstance@chat-gpt.dev.roksnet.com:5432/chatgpt_db"
)

# Путь к файлу экспорта
CSV_FILE = "interactions.csv"

# Запрос к таблице (в схеме chatdata)
SQL_QUERY = "SET search_path TO chatdata; SELECT * FROM interactions;"

def export_to_csv():
    engine = create_engine(DATABASE_URL)

    with engine.connect() as conn:
        conn.execute(text("SET search_path TO chatdata;"))
        result = conn.execute(text("SELECT * FROM interactions"))
        rows = result.fetchall()
        headers = result.keys()

        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)

    print(f"✅ Экспорт завершён: {CSV_FILE}")

if __name__ == "__main__":
    export_to_csv()