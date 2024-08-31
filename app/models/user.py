from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    fullname = Column(String, nullable=False)
    
    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")
  