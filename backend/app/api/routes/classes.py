# app/api/routes/classes.py
from fastapi import APIRouter, Depends
from app.models import Class
from app.schemas import ClassCreate, ClassResponse
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/classes/", response_model=ClassResponse)
def create_class(class_data: ClassCreate, db: Session = Depends(get_db)):
    new_class = Class(**class_data.dict())
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class

@router.get("/classes/{class_id}", response_model=ClassResponse)
def get_class(class_id: int, db: Session = Depends(get_db)):
    return db.query(Class).filter(Class.id == class_id).first()
