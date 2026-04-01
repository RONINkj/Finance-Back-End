from pydantic import BaseModel, Field
from datetime import date
from typing import Optional


class TransactionBase(BaseModel):
    amount: float = Field(gt=0)
    type: str
    category: str
    date: date
    notes: Optional[str] = None


class TransactionCreate(TransactionBase):
    pass


class TransactionResponse(TransactionBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True

