from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from app.config import Base
from pydantic import BaseModel


class Feedback(BaseModel):
    question: str
    answer: str
    feedback: str


Base = declarative_base()


class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, index=True)
    answer = Column(String)
    feedback = Column(String)
