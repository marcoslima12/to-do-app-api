from pydantic import BaseModel
from uuid import UUID


class UserBase(BaseModel):
    email: str
    fullname: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: UUID
    
    class Config:
        orm_mode = True
    