from sqlalchemy.orm import Session
from db.models import Class  # Corregida importación
from schemas.class_schema import ClassCreate
from fastapi import HTTPException

def create_class(db: Session, class_data: ClassCreate, teacher_id: int):
    db_class = Class(**class_data.dict(), teacher_id=teacher_id)
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

def get_class(db: Session, class_id: int):
    class_ = db.query(Class).filter(Class.id == class_id).first()
    if not class_:
        raise HTTPException(status_code=404, detail="Class not found")
    return class_

def delete_class(db: Session, class_id: int):
    class_ = get_class(db, class_id)
    db.delete(class_)
    db.commit()
    return {"message": "Class deleted successfully"}
