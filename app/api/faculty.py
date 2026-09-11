from fastapi import APIRouter, HTTPException

from app.schemas.faculty import (
    FacultyCreate,
    FacultyResponse
)

from app.services.faculty_service import (
    create_faculty,
    get_all_faculty,
    get_faculty_by_id,
    update_faculty,
    delete_faculty
)


router = APIRouter(
    prefix="/api/faculty",
    tags=["Faculty"]
)


@router.post("/", response_model=FacultyResponse)
def create_faculty_api(faculty: FacultyCreate):
    try:
        return create_faculty(faculty)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/", response_model=list[FacultyResponse])
def get_all_faculty_api():
    try:
        return get_all_faculty()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/{faculty_id}", response_model=FacultyResponse)
def get_faculty_api(faculty_id: str):
    faculty = get_faculty_by_id(faculty_id)

    if faculty is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty not found"
        )

    return faculty


@router.put("/{faculty_id}", response_model=FacultyResponse)
def update_faculty_api(
    faculty_id: str,
    faculty: FacultyCreate
):
    updated_faculty = update_faculty(
        faculty_id,
        faculty
    )

    if updated_faculty is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty not found"
        )

    return updated_faculty


@router.delete("/{faculty_id}")
def delete_faculty_api(faculty_id: str):
    deleted = delete_faculty(faculty_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Faculty not found"
        )

    return {
        "message": "Faculty deleted successfully"
    }