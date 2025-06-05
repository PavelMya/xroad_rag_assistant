import os
from dotenv import load_dotenv
from functools import partial
from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Загрузка .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Загрузка всех Markdown-документов
loader = DirectoryLoader(
    "data",
    glob="**/*.md",
    loader_cls=partial(TextLoader, encoding='utf-8')
)
documents = loader.load()

# Фильтрация пустых файлов
documents = [doc for doc in documents if doc.page_content.strip()]
print(f"📄 Загружено файлов: {len(documents)}")

# Вывод первых строк каждого файла (для отладки)
for doc in documents[:3]:
    print(f"\n📁 {doc.metadata['source']}")
    print(doc.page_content[:300], "...\n")

# Разделение на чанки
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
split_docs = text_splitter.split_documents(documents)
print(f"✂️ Разбито на чанки: {len(split_docs)}")

# Создание эмбеддингов
embeddings = OpenAIEmbeddings(api_key=openai_api_key)

# Построение и сохранение индекса
vectorstore = FAISS.from_documents(split_docs, embeddings)
vectorstore.save_local("faiss_index")
print("✅ Индекс сохранён в папку faiss_index.")