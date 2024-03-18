from pydantic import BaseModel
from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel


class HistoryCreate(BaseModel):
    question: str
    answer: str
