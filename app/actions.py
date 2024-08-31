from sqlalchemy.orm import Session
from app.models.user import User
from app.models.task import Task
from app.schemas.task import TaskCreate
from app.schemas.user import UserCreate


def get_user(db: Session, user_id: int):
  return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
  return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
  db_user = User(email=user.email, fullname=user.fullname)
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user

def create_task(db: Session, task: TaskCreate, user_id: int):
    db_task = Task(title=task.title, desc=task.desc, deadline=task.deadline, isDone=task.isDone, user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Task).offset(skip).limit(limit).all()

def delete_task(db: Session, task_id: int):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task 