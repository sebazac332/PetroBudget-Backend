from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from . import schemas, functions
from app.model import models

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if functions.get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="A registered user with this email already exists.")
    return functions.create_user(db, user)

@router.put("/{user_id}", response_model=schemas.User)
def edit_user(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    user = functions.update_user(db, user_id, user_update)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}", response_model=schemas.User)
def remove_user(user_id: int, db: Session = Depends(get_db)):
    user = functions.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user