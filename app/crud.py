from sqlalchemy.orm import Session
from app.models import History
from app.schemas import HistoryCreate
from fastapi import HTTPException
from sqlalchemy import desc


def add_history(db: Session, history: HistoryCreate):
    db_history = History(**history.dict())
    db.add(db_history)
    db.commit()
    db.refresh(db_history)
    return db_history


def get_history_last(db: Session):
    return db.query(History).order_by(desc(History.id)).first()


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


def update_feedback(db: Session, history_id: int, feedback: str):
    db_history = db.query(History).filter(
        History.id == history_id).first()
    if db_history:
        db_history.feedback = feedback
        db.commit()
        return db_history
    return None
