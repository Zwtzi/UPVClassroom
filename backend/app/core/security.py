# app/core/security.py
from passlib.context import CryptContext
import jwt
import datetime
from app.core.config import settings

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return password_context.verify(plain_password, hashed_password)

def hash_password(password: str) -> str:  # Mover hashing aquí
    return password_context.hash(password)

def create_access_token(data: dict, expires_delta: int = None):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_delta or settings.ACCESS_TOKEN_EXPIRE_SECONDS)
    to_encode.update({"exp": expire})
    try:
        return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    except Exception as e:
        raise Exception(f"Token generation failed: {str(e)}")