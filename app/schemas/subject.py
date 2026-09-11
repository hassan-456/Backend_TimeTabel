from pydantic import BaseModel, Field


class SubjectCreate(BaseModel):
    department_id: str = Field(..., min_length=1)
    name: str = Field(..., min_length=2, max_length=100)
    code: str = Field(..., min_length=2, max_length=20)

    lectures_per_week: int = Field(..., ge=1, le=20)

    priority: int = Field(..., ge=1, le=10)

    is_lab: bool = False


class SubjectResponse(BaseModel):
    id: str
    department_id: str
    name: str
    code: str
    lectures_per_week: int
    priority: int
    is_lab: bool