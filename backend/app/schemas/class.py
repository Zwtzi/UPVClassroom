from pydantic import BaseModel
from typing import List, Optional

class ClassBase(BaseModel):
    name: str
    description: Optional[str] = None
    group_code: str
    career: str
    semester: int

class ClassCreate(ClassBase):
    pass

class ClassResponse(ClassBase):
    id: int
    students: List[int] = []
    teacher_id: int

    class Config:
        from_attributes = True
