from uuid import UUID
from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate

def create_task(db: Session, task: TaskCreate, user_id: UUID):
    db_task = Task(title=task.title, desc=task.desc, deadline=task.deadline, isDone=task.isDone, user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, task_id: UUID):
    return db.query(Task).filter(Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Task).offset(skip).limit(limit).all()

def get_tasks_by_user(db: Session, user_id: UUID, skip: int = 0, limit: int = 10):
    return db.query(Task).filter(Task.user_id == user_id).offset(skip).limit(limit).all()

def update_task_done(db: Session, task_id: UUID, is_done: bool):
    db_task = get_task(db, task_id)
    if db_task:
        db_task.isDone = is_done
        db.commit()
        db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: UUID):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task 