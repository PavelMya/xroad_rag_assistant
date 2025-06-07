from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from chat import qa_chain

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def index():
    return FileResponse("static/index.html")

class Question(BaseModel):
    question: str

@app.post("/chat")
async def chat_endpoint(q: Question):
    result = qa_chain.invoke({"question": q.question})

    return JSONResponse({
        "answer": result.get("answer", ""),
        "task": result.get("task", ""),
        "system": result.get("system", ""),
        "symptom": result.get("symptom", ""),
        "context": result.get("context", ""),
        "confidence": result.get("confidence", ""),
        "sources": [
            doc.metadata.get("source", "Unknown")
            for doc in result.get("source_documents", [])
        ]
    })