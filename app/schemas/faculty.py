from pydantic import BaseModel, Field


class FacultyCreate(BaseModel):
    department_id: str = Field(..., min_length=1)

    name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    employee_id: str = Field(
        ...,
        min_length=2,
        max_length=30
    )

    email: str = Field(
        ...,
        min_length=5,
        max_length=100
    )

    max_lectures_per_day: int = Field(
        ...,
        ge=1,
        le=10
    )


class FacultyResponse(BaseModel):
    id: str
    department_id: str
    name: str
    employee_id: str
    email: str
    max_lectures_per_day: int