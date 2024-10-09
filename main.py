from fastapi import FastAPI
import models
from database import engine, init_db
from routers import emp, authentication

app = FastAPI()

# Initialize database
init_db()

# Include routers
app.include_router(authentication.router)
app.include_router(emp.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
