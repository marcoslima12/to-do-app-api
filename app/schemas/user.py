from typing import Optional
from pydantic import BaseModel
from uuid import UUID

class UserBase(BaseModel):
    email: str
    fullname: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    email: Optional[str] = None
    fullname: Optional[str] = None

class User(UserBase):
    id: UUID
    
    class Config:
        orm_mode = True
    