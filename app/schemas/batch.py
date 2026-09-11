from pydantic import BaseModel, Field


class BatchCreate(BaseModel):
    department_id: str = Field(..., min_length=1)
    name: str = Field(..., min_length=2, max_length=50)
    semester: int = Field(..., ge=1, le=12)
    academic_year: str = Field(..., min_length=4, max_length=20)
    student_count: int = Field(..., ge=1, le=1000)


class BatchResponse(BaseModel):
    id: str
    department_id: str
    name: str
    semester: int
    academic_year: str
    student_count: int