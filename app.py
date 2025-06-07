from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from chat import enhanced_query  # agent удалён

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def index():
    return FileResponse("static/index.html")

class Question(BaseModel):
    question: str

@app.post("/chat")
async def chat_endpoint(q: Question):
    result = enhanced_query(q.question)

    return JSONResponse({
        "answer": result.get("answer", "").strip(),
        "task": result.get("task", "").strip(),
        "system": result.get("system", "").strip(),
        "symptom": result.get("symptom", "").strip(),
        "context": result.get("context", "").strip(),
        "confidence": result.get("confidence", "").strip(),
        "sources": []  # скрыто от клиента
    })