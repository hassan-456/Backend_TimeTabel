from bson import ObjectId
from app.database import db
from app.schemas.subject import SubjectCreate


def create_subject(subject: SubjectCreate):
    subject_data = subject.model_dump()

    result = db.subjects.insert_one(subject_data)

    return {
        "id": str(result.inserted_id),
        **subject_data
    }


def get_all_subjects():
    subjects = []

    for subject in db.subjects.find():
        subjects.append({
            "id": str(subject["_id"]),
            "department_id": subject["department_id"],
            "name": subject["name"],
            "code": subject["code"],
            "lectures_per_week": subject["lectures_per_week"],
            "priority": subject["priority"],
            "is_lab": subject["is_lab"]
        })

    return subjects


def get_subject_by_id(subject_id: str):
    if not ObjectId.is_valid(subject_id):
        return None

    subject = db.subjects.find_one(
        {"_id": ObjectId(subject_id)}
    )

    if subject is None:
        return None

    return {
        "id": str(subject["_id"]),
        "department_id": subject["department_id"],
        "name": subject["name"],
        "code": subject["code"],
        "lectures_per_week": subject["lectures_per_week"],
        "priority": subject["priority"],
        "is_lab": subject["is_lab"]
    }


def update_subject(
    subject_id: str,
    subject: SubjectCreate
):
    if not ObjectId.is_valid(subject_id):
        return None

    subject_data = subject.model_dump()

    result = db.subjects.update_one(
        {"_id": ObjectId(subject_id)},
        {"$set": subject_data}
    )

    if result.matched_count == 0:
        return None

    return get_subject_by_id(subject_id)


def delete_subject(subject_id: str):
    if not ObjectId.is_valid(subject_id):
        return False

    result = db.subjects.delete_one(
        {"_id": ObjectId(subject_id)}
    )

    return result.deleted_count > 0