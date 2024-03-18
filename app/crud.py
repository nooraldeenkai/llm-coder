from sqlalchemy.orm import Session
from app.models import History
from app.schemas import HistoryCreate
from fastapi import FastAPI, HTTPException


def add_history(db: Session, history: HistoryCreate):
    db_history = History(**history.dict())
    db.add(db_history)
    db.commit()
    db.refresh(db_history)
    return db_history


def get_history(db: Session):
    return db.query(History).all()


def remove_history(db: Session, history_id: int):
    history = db.query(History).filter(History.id == history_id).first()
    if history:
        db.delete(history)
        db.commit()
        return {"message": "History deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="History not found")


def update_feedback(db: Session, response_id: int, feedback: str):
    db_response = db.query(History).filter(
        History.id == response_id).first()
    if db_response:
        db_response.feedback = feedback
        db.commit()
        return db_response
    return None
