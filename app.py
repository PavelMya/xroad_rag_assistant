
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from chat import enhanced_query
import os

app = FastAPI()

# CORS (если нужен)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Модель запроса
class QueryRequest(BaseModel):
    question: str

# Модель ответа
class QueryResponse(BaseModel):
    answer: str
    sources: list[str]

# Подключаем папку с frontend (там должен быть index.html)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Отдаём index.html при открытии корня сайта
@app.get("/")
async def serve_index():
    return FileResponse("static/index.html")

# API endpoint для общения с GPT
@app.post("/chat", response_model=QueryResponse)
async def chat_endpoint(request: QueryRequest):
    response = enhanced_query(request.question)
    return {
        "answer": response["answer"],
        "sources": response["source_documents"],
    }

# Локальный запуск
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)