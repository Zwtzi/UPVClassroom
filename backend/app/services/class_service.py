from sqlalchemy.orm import Session
from models.class_model import Class
from schemas.class_schema import ClassCreate

def create_class(db: Session, class_data: ClassCreate, teacher_id: int):
    db_class = Class(**class_data.dict(), teacher_id=teacher_id)
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

def get_class(db: Session, class_id: int):
    return db.query(Class).filter(Class.id == class_id).first()
