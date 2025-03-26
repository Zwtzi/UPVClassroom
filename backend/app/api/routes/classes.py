# app/api/routes/classes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Class, User
from app.schemas import ClassCreate, ClassResponse
from app.database import get_db
from app.api.routes.auth import get_current_user

router = APIRouter()

@router.post("/classes/", response_model=ClassResponse)
def create_class(class_data: ClassCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=403, detail="Not authorized")
    new_class = Class(**class_data.dict(), teacher_id=current_user.id)
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class

@router.get("/classes/{class_id}", response_model=ClassResponse)
def get_class(class_id: int, db: Session = Depends(get_db)):
    class_ = db.query(Class).filter(Class.id == class_id).first()
    if not class_:
        raise HTTPException(status_code=404, detail="Class not found")
    return class_