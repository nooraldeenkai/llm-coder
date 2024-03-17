from sqlalchemy.orm import Session
from app.models import History
from app.schemas import HistorySchema


def get_history(db: Session, skip: int = 0, limit: int = 100):
    return db.query(History).offset(skip).limit(limit).all()


def get_history_by_id(db: Session, history_id: int):
    return db.query(History).filter(History.id == history_id).first()


def create_history(db: Session, history: HistorySchema):
    _history = history(question=history.question, answer=history.answer)
    db.add(_history)
    db.commit()
    db.refresh(_history)
    return _history


def remove_history(db: Session, history_id: int):
    _history = get_history_by_id(db=db, history_id=history_id)
    db.delete(_history)
    db.commit()


def update_history(db: Session, history_id: int, question: str, answer: str):
    _history = get_history_by_id(db=db, history_id=history_id)

    _history.question = question
    _history.answer = answer

    db.commit()
    db.refresh(_history)
    return _history
