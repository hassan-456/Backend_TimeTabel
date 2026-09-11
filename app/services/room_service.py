from bson import ObjectId

from app.database import db
from app.schemas.room import RoomCreate


def create_room(room: RoomCreate):
    room_data = room.model_dump()

    result = db.rooms.insert_one(room_data)

    return {
        "id": str(result.inserted_id),
        **room_data
    }


def get_all_rooms():
    rooms = []

    for room in db.rooms.find():
        rooms.append({
            "id": str(room["_id"]),
            "name": room["name"],
            "capacity": room["capacity"],
            "room_type": room["room_type"],
            "building": room["building"]
        })

    return rooms


def get_room_by_id(room_id: str):
    if not ObjectId.is_valid(room_id):
        return None

    room = db.rooms.find_one(
        {"_id": ObjectId(room_id)}
    )

    if room is None:
        return None

    return {
        "id": str(room["_id"]),
        "name": room["name"],
        "capacity": room["capacity"],
        "room_type": room["room_type"],
        "building": room["building"]
    }


def update_room(
    room_id: str,
    room: RoomCreate
):
    if not ObjectId.is_valid(room_id):
        return None

    room_data = room.model_dump()

    result = db.rooms.update_one(
        {"_id": ObjectId(room_id)},
        {"$set": room_data}
    )

    if result.matched_count == 0:
        return None

    return get_room_by_id(room_id)


def delete_room(room_id: str):
    if not ObjectId.is_valid(room_id):
        return False

    result = db.rooms.delete_one(
        {"_id": ObjectId(room_id)}
    )

    return result.deleted_count > 0