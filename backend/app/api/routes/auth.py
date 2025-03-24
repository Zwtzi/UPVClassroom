
# app/api/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException
from app.models import User
from app.schemas import UserLogin, Token
from app.database import get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import jwt
import datetime

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()

@router.post("/auth/token", response_model=Token)
def login_for_access_token(user_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_data.email).first()
    if not user or not password_context.verify(user_data.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    token_data = {"sub": user.email, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)}
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}
