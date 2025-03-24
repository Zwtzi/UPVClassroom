# app/models/material.py
from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Material(Base):
    __tablename__ = "materials"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    file_url = Column(String)
    class_id = Column(Integer, ForeignKey("classes.id"))
