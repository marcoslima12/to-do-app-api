from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.actions.task import create_task, delete_task, get_task, get_tasks, get_tasks_by_user
from app.schemas.task import Task, TaskCreate
from app.database import get_db

router = APIRouter()

@router.post("/createTask/{user_id}", response_model=Task)
def create_tasks(task: TaskCreate, user_id: UUID, db: Session = Depends(get_db)):
    return create_task(db, task, user_id=user_id)

@router.get("/{task_id}", response_model=Task)
def read_task(task_id: UUID, db: Session = Depends(get_db)):
    db_task = get_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.get("/", response_model=list[Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_tasks(db, skip=skip, limit=limit)

@router.get("/user/{user_id}", response_model=list[Task])
def read_tasks_by_user_route(user_id: UUID, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tasks = get_tasks_by_user(db, user_id=user_id, skip=skip, limit=limit)
    return tasks

@router.put("/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    db_task = update_task(db, task_id, task)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.delete("/{task_id}", response_model=Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = delete_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
