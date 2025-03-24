# app/api/routes/users.py
from fastapi import APIRouter, Depends
from app.models import User
from app.schemas import UserCreate, UserResponse
from app.database import get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext

router = APIRouter()
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/users/", response_model=UserResponse)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    hashed_password = password_context.hash(user_data.password)
    new_user = User(**user_data.dict(), password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == user_id).first()
