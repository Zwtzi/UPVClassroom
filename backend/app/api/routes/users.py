# app/api/routes/users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate, UserResponse
from app.database import get_db
from app.api.routes.auth import get_current_user
from passlib.context import CryptContext

router = APIRouter()
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/users/", response_model=UserResponse)
def create_user(user_data: UserCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=403, detail="Not authorized")
    hashed_password = password_context.hash(user_data.password)
    new_user = User(username=user_data.username, email=user_data.email, full_name=user_data.full_name, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
