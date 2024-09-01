from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.actions.user import delete_user, get_user_by_email, get_users, create_user, get_user, update_user
from app.schemas.user import User, UserCreate, UserUpdate
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=User)
def create_users(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@router.get("/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=User)
def read_user(user_id: UUID, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.patch("/{user_id}", response_model=User)
def update_user_route(user_id: UUID, user_update: UserUpdate, db: Session = Depends(get_db)):
    db_user = update_user(db, user_id=user_id, user=user_update)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/email/{email}", response_model=User)
def read_user_by_email(email: str, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}", response_model=User)
def delete_users(user_id: UUID, db: Session = Depends(get_db)):
    db_user = delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
