from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from chat import qa_chain, agent  # теперь импортируем и agent

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def index():
    return FileResponse("static/index.html")

class Question(BaseModel):
    question: str

@app.post("/chat")
async def chat_endpoint(q: Question):
    # Пытаемся получить структурированный ответ от RAG
    from chat import enhanced_query
    result = enhanced_query(q.question)
    answer = result.get("answer", "").strip()
    task = result.get("task", "").strip()

    # Если RAG не дал ответ (например, вообще не понял вопрос) — fallback на function-calling
    if not answer or answer.lower().startswith("i don't know") or (not task and "error" in answer.lower()):
        try:
            agent_answer = agent.run(q.question)
            return JSONResponse({
                "answer": f"🛠️ {agent_answer}",
                "task": "Function calling",
                "system": "",
                "symptom": "",
                "context": "",
                "confidence": "High",
                "sources": []
            })
        except Exception as e:
            return JSONResponse({
                "answer": f"⚠️ Function tool failed: {str(e)}",
                "task": "Function call failed",
                "system": "",
                "symptom": "",
                "context": "",
                "confidence": "Low",
                "sources": []
            })

    # Если всё нормально — отдаем как есть
    return JSONResponse({
        "answer": answer,
        "task": task,
        "system": result.get("system", ""),
        "symptom": result.get("symptom", ""),
        "context": result.get("context", ""),
        "confidence": result.get("confidence", ""),
        "sources": [
            doc.metadata.get("source", "Unknown")
            for doc in result.get("source_documents", [])
        ]
    })