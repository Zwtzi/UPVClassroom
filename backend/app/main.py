from fastapi import FastAPI
from app.db.database import engine, Base
from app.api.routes import users, classes, tasks, auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="UPV Classroom API", version="1.0")

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(classes.router, prefix="/classes", tags=["Classes"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def root():
    return {"message": "Welcome to UPV Classroom API"}
