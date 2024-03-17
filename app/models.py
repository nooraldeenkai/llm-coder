from sqlalchemy import Column, Integer, String
from app.config import Base
from pydantic import BaseModel


class Feedback(BaseModel):
    question: str
    answer: str
    feedback: str
