from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chat import enhanced_query  # импорт функции из chat.py

app = FastAPI()

# Разрешим CORS (если frontend на другом домене)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # можешь указать конкретный frontend-домен
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Модель запроса от клиента
class QueryRequest(BaseModel):
    question: str

# Модель ответа
class QueryResponse(BaseModel):
    answer: str
    sources: list[str]

# Главный endpoint
@app.post("/chat", response_model=QueryResponse)
async def chat_endpoint(request: QueryRequest):
    response = enhanced_query(request.question)
    return {
        "answer": response["answer"],
        "sources": response["source_documents"],
    }

# Для локального запуска
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

@app.get("/")
def root():
    return {"message": "ChatGPT assistant is running. Use POST /chat to interact."}