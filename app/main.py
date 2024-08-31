from fastapi import FastAPI
from app.database import Base, engine
from app.routers import user, task

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Server running..."}
  
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(task.router, prefix="/tasks", tags=["tasks"])
