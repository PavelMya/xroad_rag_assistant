import os
from dotenv import load_dotenv
from functools import partial
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Загрузка переменных из .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Загрузка документов из всех подпапок data/
loader = DirectoryLoader(
    "data",
    glob="**/*.md",
    loader_cls=partial(TextLoader, encoding='utf-8')
)
documents = loader.load()
print(f"Загружено файлов: {len(documents)}")

# Разделение на чанки
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
split_docs = text_splitter.split_documents(documents)
print(f"Разбито на чанки: {len(split_docs)}")

# Создание эмбеддингов и FAISS-индекса
embeddings = OpenAIEmbeddings(api_key=openai_api_key)
vectorstore = FAISS.from_texts([doc.page_content for doc in split_docs], embeddings)

# Сохраняем FAISS базу
vectorstore.save_local("faiss_index")
print("Индекс сохранён в папку faiss_index.")