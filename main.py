import os
import logging
import argparse
from dotenv import load_dotenv
from pathlib import Path
from tqdm import tqdm
from functools import partial

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Настройка логгера
logging.basicConfig(filename="build_faiss.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Парсинг аргументов
parser = argparse.ArgumentParser(description="Build FAISS index from X-Road documentation")
parser.add_argument("--data_dir", default="xroad_documentation", help="Directory with .md files")
parser.add_argument("--index_dir", default="faiss_index", help="Where to save FAISS index")
args = parser.parse_args()

# Загрузка .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY не найден в .env")

# Загрузка документов
data_path = Path(args.data_dir)
if not data_path.exists():
    raise FileNotFoundError(f"Папка {data_path} не найдена")

loader = DirectoryLoader(
    str(data_path),
    glob="**/*.md",
    loader_cls=partial(TextLoader, encoding="utf-8")
)
docs = loader.load()
logging.info(f"Загружено файлов: {len(docs)}")
print(f"📘 Загружено файлов: {len(docs)}")

# Чанки
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)
logging.info(f"Разбито на чанки: {len(chunks)}")
print(f"✂️ Разбито на чанки: {len(chunks)}")

# Эмбеддинги и FAISS
embeddings = OpenAIEmbeddings(api_key=api_key)

print("💾 Генерация векторной базы FAISS...")
vectorstore = FAISS.from_documents(tqdm(chunks, desc="Embedding chunks"), embeddings)

# Сохраняем
index_dir = args.index_dir
vectorstore.save_local(index_dir)
logging.info(f"Индекс сохранён в: {index_dir}")
print(f"✅ FAISS индекс успешно сохранён в: {index_dir}")