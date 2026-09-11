from fastapi import FastAPI

from app.database import client
from app.api.departments import router as department_router
from app.api.batches import router as batch_router
from app.api.subjects import router as subject_router
from app.api.faculty import router as faculty_router
from app.api.rooms import router as room_router

app = FastAPI(
    title="College Timetable AI",
    description="AI-based college timetable generation system",
    version="1.0.0"
)

app.include_router(department_router)
app.include_router(batch_router)
app.include_router(subject_router)
app.include_router(faculty_router)
app.include_router(room_router)

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