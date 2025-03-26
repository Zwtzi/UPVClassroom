from sqlalchemy.orm import Session
from db.models import Task  # Corregida importación
from schemas.task import TaskCreate
from fastapi import HTTPException

def create_task(db: Session, task_data: TaskCreate, class_id: int):
    db_task = Task(**task_data.dict(), class_id=class_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

def delete_task(db: Session, task_id: int):
    task = get_task(db, task_id)
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}
