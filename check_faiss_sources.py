import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

print("🔍 Старт...")

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("⚠️ OPENAI_API_KEY не найден, продолжаем без него...")

index_dir = "faiss_index"
print(f"📁 Путь к индексу: {index_dir}")

# Проверим наличие файлов
faiss_file = os.path.join(index_dir, "index.faiss")
pkl_file = os.path.join(index_dir, "index.pkl")

if not os.path.exists(faiss_file):
    print(f"❌ Файл index.faiss не найден по пути: {faiss_file}")
if not os.path.exists(pkl_file):
    print(f"❌ Файл index.pkl не найден по пути: {pkl_file}")

# Пробуем загрузить
try:
    print("📦 Загружаем FAISS индекс...")
    vectorstore = FAISS.load_local(index_dir, OpenAIEmbeddings(), allow_dangerous_deserialization=True)
    print("✅ Индекс успешно загружен.")
except Exception as e:
    print(f"❌ Ошибка при загрузке индекса: {e}")
    exit(1)

docs = vectorstore.docstore._dict.values()
print(f"📄 Загружено чанков: {len(docs)}")

# Список файлов
sources = sorted({doc.metadata.get("source", "нет source") for doc in docs})
print(f"📚 Найдено файлов: {len(sources)}")
for src in sources:
    print("—", src)

# Поиск по "web portal"
print("\n🔎 Ищем 'web portal' в содержимом...")
found = False
for doc in docs:
    content = doc.page_content.lower()
    if "web portal" in content or "веб портал" in content:
        found = True
        print(f"\n✅ Найдено в файле: {doc.metadata.get('source', 'нет source')}")
        print("🔹 Отрывок:\n", content[:400], "...\n")

if not found:
    print("❌ Не найдено упоминаний 'web portal'")