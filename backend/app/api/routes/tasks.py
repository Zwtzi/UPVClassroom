
# app/api/routes/tasks.py
from fastapi import APIRouter, Depends
from app.models import Task
from app.schemas import TaskCreate, TaskResponse
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/tasks/", response_model=TaskResponse)
def create_task(task_data: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(**task_data.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return db.query(Task).filter(Task.id == task_id).first()
