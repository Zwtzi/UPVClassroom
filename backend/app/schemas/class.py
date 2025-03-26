from pydantic import BaseModel
from typing import Optional

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
    teacher_id: int  # Se mantiene porque sí está en `models.py`

    class Config:
        from_attributes = True
