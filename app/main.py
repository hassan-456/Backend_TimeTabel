from fastapi import FastAPI

app = FastAPI(
    title="College Timetable AI",
    description="AI-based college timetable generation system",
    version="1.0.0"
)

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