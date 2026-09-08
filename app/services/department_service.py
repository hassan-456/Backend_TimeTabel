# this are the api that we have to craete in this 
# POST    /api/departments
# GET     /api/departments
# GET     /api/departments/{id}
# PUT     /api/departments/{id}
# DELETE  /api/departments/{id}

from bson import ObjectId

from app.database import db
from app.schemas.department import DepartmentCreate


def create_department(department: DepartmentCreate):
    department_data = department.model_dump()

    result = db.departments.insert_one(department_data)

    return {
        "id": str(result.inserted_id),
        **department_data
    }


def get_all_departments():
    departments = []

    for department in db.departments.find():
        departments.append({
            "id": str(department["_id"]),
            "name": department["name"],
            "code": department["code"],
            "description": department.get("description")
        })

    return departments


def get_department_by_id(department_id: str):
    if not ObjectId.is_valid(department_id):
        return None

    department = db.departments.find_one(
        {"_id": ObjectId(department_id)}
    )

    if department is None:
        return None

    return {
        "id": str(department["_id"]),
        "name": department["name"],
        "code": department["code"],
        "description": department.get("description")
    }


def update_department(
    department_id: str,
    department: DepartmentCreate
):
    if not ObjectId.is_valid(department_id):
        return None

    department_data = department.model_dump()

    result = db.departments.update_one(
        {"_id": ObjectId(department_id)},
        {"$set": department_data}
    )

    if result.matched_count == 0:
        return None

    return get_department_by_id(department_id)


def delete_department(department_id: str):
    if not ObjectId.is_valid(department_id):
        return False

    result = db.departments.delete_one(
        {"_id": ObjectId(department_id)}
    )

    return result.deleted_count > 0