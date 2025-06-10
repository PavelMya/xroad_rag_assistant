from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from chat import enhanced_query
from database import mark_incorrect, save_suggested_answer  # 🆕
import os

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MODELS ---
class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
    sources: list[str]
    question_id: str

class IncorrectFeedback(BaseModel):
    question_id: str

class SuggestFeedback(BaseModel):
    question_id: str
    suggested_answer: str

# --- STATIC FILES ---
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def serve_index():
    return FileResponse("static/index.html")

# --- MAIN CHAT ENDPOINT ---
@app.post("/chat", response_model=QueryResponse)
async def chat_endpoint(request: QueryRequest):
    response = enhanced_query(request.question)
    return {
        "answer": response["answer"],
        "sources": [],
        "question_id": response["question_id"]
    }

# --- FEEDBACK ENDPOINTS ---
@app.post("/feedback/incorrect")
async def feedback_incorrect(feedback: IncorrectFeedback):
    mark_incorrect(feedback.question_id)
    return {"status": "ok", "message": "Marked as incorrect"}

@app.post("/feedback/suggest")
async def feedback_suggest(feedback: SuggestFeedback):
    save_suggested_answer(feedback.question_id, feedback.suggested_answer)
    return {"status": "ok", "message": "Suggestion saved"}

# --- DEV SERVER ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
