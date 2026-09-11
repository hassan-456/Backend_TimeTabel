from fastapi import APIRouter, HTTPException

from app.schemas.subject import (
    SubjectCreate,
    SubjectResponse
)

from app.services.subject_service import (
    create_subject,
    get_all_subjects,
    get_subject_by_id,
    update_subject,
    delete_subject
)


router = APIRouter(
    prefix="/api/subjects",
    tags=["Subjects"]
)


@router.post("/", response_model=SubjectResponse)
def create_subject_api(subject: SubjectCreate):
    try:
        return create_subject(subject)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/", response_model=list[SubjectResponse])
def get_all_subjects_api():
    try:
        return get_all_subjects()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/{subject_id}", response_model=SubjectResponse)
def get_subject_api(subject_id: str):
    subject = get_subject_by_id(subject_id)

    if subject is None:
        raise HTTPException(
            status_code=404,
            detail="Subject not found"
        )

    return subject


@router.put("/{subject_id}", response_model=SubjectResponse)
def update_subject_api(
    subject_id: str,
    subject: SubjectCreate
):
    updated_subject = update_subject(
        subject_id,
        subject
    )

    if updated_subject is None:
        raise HTTPException(
            status_code=404,
            detail="Subject not found"
        )

    return updated_subject


@router.delete("/{subject_id}")
def delete_subject_api(subject_id: str):
    deleted = delete_subject(subject_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Subject not found"
        )

    return {
        "message": "Subject deleted successfully"
    }