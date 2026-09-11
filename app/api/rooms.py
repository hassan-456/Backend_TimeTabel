from fastapi import APIRouter, HTTPException

from app.schemas.room import (
    RoomCreate,
    RoomResponse
)

from app.services.room_service import (
    create_room,
    get_all_rooms,
    get_room_by_id,
    update_room,
    delete_room
)


router = APIRouter(
    prefix="/api/rooms",
    tags=["Rooms"]
)


@router.post("/", response_model=RoomResponse)
def create_room_api(room: RoomCreate):
    try:
        return create_room(room)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/", response_model=list[RoomResponse])
def get_all_rooms_api():
    try:
        return get_all_rooms()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/{room_id}", response_model=RoomResponse)
def get_room_api(room_id: str):
    room = get_room_by_id(room_id)

    if room is None:
        raise HTTPException(
            status_code=404,
            detail="Room not found"
        )

    return room


@router.put("/{room_id}", response_model=RoomResponse)
def update_room_api(
    room_id: str,
    room: RoomCreate
):
    updated_room = update_room(
        room_id,
        room
    )

    if updated_room is None:
        raise HTTPException(
            status_code=404,
            detail="Room not found"
        )

    return updated_room


@router.delete("/{room_id}")
def delete_room_api(room_id: str):
    deleted = delete_room(room_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Room not found"
        )

    return {
        "message": "Room deleted successfully"
    }