from pydantic import BaseModel
from typing import Optional

class ItemCreate(BaseModel):
    name: str
    category: Optional[str] = "Other"

class ItemUpdate(BaseModel):
    name: Optional[str]
    category: Optional[str]
    purchased: Optional[bool]

class ItemOut(BaseModel):
    id: int
    name: str
    category: str
    purchased: bool

    class Config:
        orm_mode = True

