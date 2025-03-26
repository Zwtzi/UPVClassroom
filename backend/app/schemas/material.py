from pydantic import BaseModel
from typing import Optional

class MaterialBase(BaseModel):
    title: str
    description: Optional[str] = None
    class_id: int  # Se corrigió `topic_id` a `class_id`

class MaterialCreate(MaterialBase):
    pass

class MaterialResponse(MaterialBase):
    id: int

    class Config:
        from_attributes = True
