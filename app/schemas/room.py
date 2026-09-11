from pydantic import BaseModel, Field


class RoomCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )

    capacity: int = Field(
        ...,
        ge=1,
        le=1000
    )

    room_type: str = Field(
        ...,
        min_length=3,
        max_length=20
    )

    building: str = Field(
        ...,
        min_length=1,
        max_length=100
    )


class RoomResponse(BaseModel):
    id: str
    name: str
    capacity: int
    room_type: str
    building: str