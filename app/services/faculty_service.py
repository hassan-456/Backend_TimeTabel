from bson import ObjectId

from app.database import db
from app.schemas.faculty import FacultyCreate


def create_faculty(faculty: FacultyCreate):
    faculty_data = faculty.model_dump()

    result = db.faculty.insert_one(faculty_data)

    return {
        "id": str(result.inserted_id),
        **faculty_data
    }


def get_all_faculty():
    faculty_list = []

    for faculty in db.faculty.find():
        faculty_list.append({
            "id": str(faculty["_id"]),
            "department_id": faculty["department_id"],
            "name": faculty["name"],
            "employee_id": faculty["employee_id"],
            "email": faculty["email"],
            "max_lectures_per_day": faculty["max_lectures_per_day"]
        })

    return faculty_list


def get_faculty_by_id(faculty_id: str):
    if not ObjectId.is_valid(faculty_id):
        return None

    faculty = db.faculty.find_one(
        {"_id": ObjectId(faculty_id)}
    )

    if faculty is None:
        return None

    return {
        "id": str(faculty["_id"]),
        "department_id": faculty["department_id"],
        "name": faculty["name"],
        "employee_id": faculty["employee_id"],
        "email": faculty["email"],
        "max_lectures_per_day": faculty["max_lectures_per_day"]
    }


def update_faculty(
    faculty_id: str,
    faculty: FacultyCreate
):
    if not ObjectId.is_valid(faculty_id):
        return None

    faculty_data = faculty.model_dump()

    result = db.faculty.update_one(
        {"_id": ObjectId(faculty_id)},
        {"$set": faculty_data}
    )

    if result.matched_count == 0:
        return None

    return get_faculty_by_id(faculty_id)


def delete_faculty(faculty_id: str):
    if not ObjectId.is_valid(faculty_id):
        return False

    result = db.faculty.delete_one(
        {"_id": ObjectId(faculty_id)}
    )

    return result.deleted_count > 0