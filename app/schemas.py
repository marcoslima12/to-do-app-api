from datetime import date
from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    email: str
    fullname: str

class User(UserBase):
    id: int
    
    class Config:
        orm_mode = True
        
class TaskBase(BaseModel):
    title: str
    desc: Optional[str] = None
    deadline: date
    isDone: bool = False

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    user_id: int
    
    class Config:
        orm_mode = True