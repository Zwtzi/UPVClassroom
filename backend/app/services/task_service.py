from sqlalchemy.orm import Session
from models.task import Task
from schemas.task import TaskCreate

def create_task(db: Session, task_data: TaskCreate, class_id: int):
    db_task = Task(**task_data.dict(), class_id=class_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()
