from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./database.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(String, nullable=False)  # Nuevo campo para roles (profesor/estudiante)

    classes = relationship("Class", back_populates="teacher")
    submissions = relationship("Submission", back_populates="student")

class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    group_code = Column(String, unique=True, index=True)
    career = Column(String, nullable=False)
    semester = Column(Integer, nullable=False)
    teacher_id = Column(Integer, ForeignKey("users.id"))

    teacher = relationship("User", back_populates="classes")
    tasks = relationship("Task", back_populates="class_")
    materials = relationship("Material", back_populates="class_")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    instructions = Column(Text, nullable=False)
    due_date = Column(DateTime, nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"))

    class_ = relationship("Class", back_populates="tasks")
    submissions = relationship("Submission", back_populates="task")

class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    class_id = Column(Integer, ForeignKey("classes.id"))

    class_ = relationship("Class", back_populates="materials")

class Submission(Base):  # Nueva tabla para entregas de tareas
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    student_id = Column(Integer, ForeignKey("users.id"))
    file_url = Column(String, nullable=False)
    submitted_at = Column(DateTime, default=datetime.utcnow)

    task = relationship("Task", back_populates="submissions")
    student = relationship("User", back_populates="submissions")
