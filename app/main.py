from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.auth.router import router as auth_router
from app.role.router import router as role_router
from app.todo.router import router as todo_router
from .db import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    create_db_and_tables()
    yield
    # shutdown
    
app = FastAPI(lifespan=lifespan)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(role_router, prefix="/roles", tags=["role"])
app.include_router(todo_router, prefix="/todos", tags=["todo"])

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
