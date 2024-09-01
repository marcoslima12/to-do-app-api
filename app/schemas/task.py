from datetime import date
from typing import Optional
from uuid import UUID
from pydantic import BaseModel
        
class TaskBase(BaseModel):
    title: str
    desc: Optional[str] = None
    deadline: date
    isDone: bool = False

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: UUID
    user_id: UUID
    
    class Config:
        orm_mode = True