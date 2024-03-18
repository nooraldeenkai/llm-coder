from pydantic import BaseModel
from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel


class HistoryCreate(BaseModel):
    id: Optional[int] = None
    question: Optional[str]
    answer: Optional[str]
    feedback: Optional[str] = None


class HistoryResponse(BaseModel):
    id: int
    question: Optional[str]
    answer: Optional[str]
    feedback: Optional[str] = None
