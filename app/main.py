from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from app.actions.user import get_users, create_user, get_user
from app.actions.task import create_task, delete_task, get_task, get_tasks
from app.schemas.task import Task, TaskCreate
from app.schemas.user import User, UserCreate
from .database import Base, SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
  db = SessionLocal()

  try:
    yield db
  finally:
    db.close()

@app.get("/")
def read_root():
    return {"Server done and running..."}


@app.post("/users/", response_model=User)
def create_users(user: UserCreate, db: Session = Depends(get_db)):
  return create_user(db=db, user=user)

@app.get("/users/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  users = get_users(db, skip=skip, limit=limit)
  return users

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
  db_user = get_user(db, user_id=user_id)
  if db_user is None:
    raise HTTPException(status_code=404, detail="User not found")
  return db_user

@app.post("/tasks/", response_model=Task)
def create_tasks(task: TaskCreate, user_id: int, db: Session = Depends(get_db)):
    return create_task(db, task, user_id=user_id)

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = get_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.get("/tasks/", response_model=list[Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_tasks(db, skip=skip, limit=limit)

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    db_task = update_task(db, task_id, task)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = delete_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task