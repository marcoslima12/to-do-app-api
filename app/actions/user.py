from uuid import UUID
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

def get_user(db: Session, user_id: UUID):
  return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
  return db.query(User).offset(skip).limit(limit).all()


def get_user_by_email(db: Session, email: str) -> User | None:
  return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
  db_user = User(email=user.email, fullname=user.fullname)
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user

def delete_user(db: Session, user_id: UUID):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user