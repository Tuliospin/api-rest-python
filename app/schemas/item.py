from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ItemCreate(BaseModel):
    title: str
    description: Optional[str] = None
    price: float


class ItemOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    price: float
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
