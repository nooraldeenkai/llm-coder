import logging
from app.models import Feedback
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends
from app.config import SessionLocal
from sqlalchemy.orm import Session
from fastapi import FastAPI
from app import models
from app.services import get_answer, submit_feedback
from app.crud import add_history, get_history, remove_history
from app.config import engine, get_db
from app.schemas import HistoryCreate
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
    answer = get_answer(prompt)
    history = HistoryCreate(question=prompt, answer=answer)
    add_history(db=db, history=history)
    return answer


@app.post("/feedback")
async def receive_feedback(feedback: HistoryCreate, ):
    # Here you can process the received feedback
    # For now, we'll just print it
    reply = submit_feedback(feedback)
    print(f"Received feedback: {feedback}")
    return {"message": reply}


@app.get("/get_history")
async def history(db: Session = Depends(get_db)):
    """
    function to get the history of the user's generated code and the user's question.
    """
    history = get_history(db)
    return history


@app.delete("/delete_history")
async def delete(history_id: int , db: Session = Depends(get_db)):
    """
    function to delete the history of the user's generated code and the user's question. 
    """
    remove_history(db=db, history_id=history_id)
    return None
