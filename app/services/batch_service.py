from bson import ObjectId

from app.database import db
from app.schemas.batch import BatchCreate


def create_batch(batch: BatchCreate):
    batch_data = batch.model_dump()

    result = db.batches.insert_one(batch_data)

    return {
        "id": str(result.inserted_id),
        **batch_data
    }


def get_all_batches():
    batches = []

    for batch in db.batches.find():
        batches.append({
            "id": str(batch["_id"]),
            "department_id": batch["department_id"],
            "name": batch["name"],
            "semester": batch["semester"],
            "academic_year": batch["academic_year"],
            "student_count": batch["student_count"]
        })

    return batches


def get_batch_by_id(batch_id: str):
    if not ObjectId.is_valid(batch_id):
        return None

    batch = db.batches.find_one(
        {"_id": ObjectId(batch_id)}
    )

    if batch is None:
        return None

    return {
        "id": str(batch["_id"]),
        "department_id": batch["department_id"],
        "name": batch["name"],
        "semester": batch["semester"],
        "academic_year": batch["academic_year"],
        "student_count": batch["student_count"]
    }


def update_batch(
    batch_id: str,
    batch: BatchCreate
):
    if not ObjectId.is_valid(batch_id):
        return None

    batch_data = batch.model_dump()

    result = db.batches.update_one(
        {"_id": ObjectId(batch_id)},
        {"$set": batch_data}
    )

    if result.matched_count == 0:
        return None

    return get_batch_by_id(batch_id)


def delete_batch(batch_id: str):
    if not ObjectId.is_valid(batch_id):
        return False

    result = db.batches.delete_one(
        {"_id": ObjectId(batch_id)}
    )

    return result.deleted_count > 0