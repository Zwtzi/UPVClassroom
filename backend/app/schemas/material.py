from pydantic import BaseModel
from typing import Optional

class MaterialBase(BaseModel):
    title: str
    description: Optional[str] = None
    topic_id: int

class MaterialCreate(MaterialBase):
    pass

class MaterialResponse(MaterialBase):
    id: int
    class_id: int

    class Config:
        from_attributes = True
