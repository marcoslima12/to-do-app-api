from datetime import date
from http.client import HTTPException
from uuid import UUID
from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

def get_task(db: Session, task_id: UUID):
    return db.query(Task).filter(Task.id == task_id).first()

def get_tasks_by_user(db: Session, user_id: UUID, skip: int = 0, limit: int = 10):
    return db.query(Task).filter(Task.user_id == user_id).offset(skip).limit(limit).all()

def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Task).offset(skip).limit(limit).all()

def create_task(db: Session, task: TaskCreate, user_id: UUID):
    db_task = Task(title=task.title, desc=task.desc, deadline=task.deadline, isDone=task.isDone, user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: UUID, task: TaskUpdate):
    db_task = get_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    for key, value in task.model_dump(exclude_unset=True).items():
        setattr(db_task, key, value)
        
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: UUID):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(db_task)
    db.commit()
    return db_task 