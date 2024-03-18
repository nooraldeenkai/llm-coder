from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, HTTPException
from app.config import SessionLocal
from sqlalchemy.orm import Session
from fastapi import FastAPI
from app import models
from app.services import get_answer
from app.crud import add_history, get_history, remove_history, update_feedback, get_history_last
from app.config import engine, get_db
from app.schemas import HistoryCreate, HistoryResponse
from fastapi.staticfiles import StaticFiles

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="static"), name="index.html")


@app.post("/get_answer")
async def code_generation(prompt: str, db: Session = Depends(get_db)):
    """
    function to send the question to the LLM and get back the text response
    """
    conv_history = get_history_last(db)
    answer = get_answer(prompt, conv_history=conv_history)
    history = HistoryCreate(
        question=prompt, answer=answer, conv_history=conv_history)
    add_history(db=db, history=history)
    return answer


@app.post("/history/{history_id}/feedback", response_model=HistoryResponse)
def update_history_feedback(history_id: int, feedback: str, db: Session = Depends(get_db)):
    db_history = update_feedback(
        db=db, history_id=history_id, feedback=feedback)
    if db_history is None:
        raise HTTPException(status_code=404, detail="History not found")
    return db_history


@app.get("/get_history")
async def history(db: Session = Depends(get_db)):
    """
    function to get the history of the user's generated code and the user's question.
    """
    history = get_history(db)
    return history


@app.delete("/delete_history")
async def delete(history_id: int, db: Session = Depends(get_db)):
    """
    function to delete the history of the user's generated code and the user's question. 
    """
    remove_history(db=db, history_id=history_id)
    return None
