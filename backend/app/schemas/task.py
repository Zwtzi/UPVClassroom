from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskBase(BaseModel):
    title: str
    instructions: str
    due_date: datetime
    class_id: int  # Se corrigió `topic_id` a `class_id`

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int

    class Config:
        from_attributes = True
        json_encoders = {datetime: lambda v: v.isoformat()}  # Formato ISO 8601
