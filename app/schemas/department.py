from pydantic import BaseModel, Field
from typing import Optional

class DepartmentCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    code: str = Field(..., min_length=2, max_length=20)
    description: Optional[str] = None

class DepartmentResponse(BaseModel):
    id: str
    name: str
    code: str
    description: Optional[str] = None