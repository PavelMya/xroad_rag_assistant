from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chat import enhanced_query

app = FastAPI()

# 🌐 Разрешить CORS для браузеров
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    question: str

@app.get("/")
async def root():
    return {"message": "X-Road Assistant is live!"}

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    response = enhanced_query(request.question)
    return {"answer": response["answer"]}