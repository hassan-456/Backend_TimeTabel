from fastapi import FastAPI

from app.database import client
from app.api.departments import router as department_router


app = FastAPI(
    title="College Timetable AI",
    description="AI-based college timetable generation system",
    version="1.0.0"
)


app.include_router(department_router)


@app.get("/")
def root():
    return {
        "message": "College Timetable AI API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }