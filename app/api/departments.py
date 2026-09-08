from fastapi import APIRouter, HTTPException

from app.schemas.department import (
    DepartmentCreate,
    DepartmentResponse
)

from app.services.department_service import (
    create_department,
    get_all_departments,
    get_department_by_id,
    update_department,
    delete_department
)


router = APIRouter(
    prefix="/api/departments",
    tags=["Departments"]
)


@router.post("/", response_model=DepartmentResponse)
def create_department_api(department: DepartmentCreate):
    try:
        return create_department(department)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/", response_model=list[DepartmentResponse])
def get_all_departments_api():
    try:
        return get_all_departments()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/{department_id}", response_model=DepartmentResponse)
def get_department_api(department_id: str):
    department = get_department_by_id(department_id)

    if department is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return department


@router.put("/{department_id}", response_model=DepartmentResponse)
def update_department_api(
    department_id: str,
    department: DepartmentCreate
):
    updated_department = update_department(
        department_id,
        department
    )

    if updated_department is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return updated_department


@router.delete("/{department_id}")
def delete_department_api(department_id: str):
    deleted = delete_department(department_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return {
        "message": "Department deleted successfully"
    }