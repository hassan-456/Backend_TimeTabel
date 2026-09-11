from fastapi import APIRouter, HTTPException

from app.schemas.batch import (
    BatchCreate,
    BatchResponse
)

from app.services.batch_service import (
    create_batch,
    get_all_batches,
    get_batch_by_id,
    update_batch,
    delete_batch
)


router = APIRouter(
    prefix="/api/batches",
    tags=["Batches"]
)


@router.post("/", response_model=BatchResponse)
def create_batch_api(batch: BatchCreate):
    try:
        return create_batch(batch)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/", response_model=list[BatchResponse])
def get_all_batches_api():
    try:
        return get_all_batches()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/{batch_id}", response_model=BatchResponse)
def get_batch_api(batch_id: str):
    batch = get_batch_by_id(batch_id)

    if batch is None:
        raise HTTPException(
            status_code=404,
            detail="Batch not found"
        )

    return batch


@router.put("/{batch_id}", response_model=BatchResponse)
def update_batch_api(
    batch_id: str,
    batch: BatchCreate
):
    updated_batch = update_batch(
        batch_id,
        batch
    )

    if updated_batch is None:
        raise HTTPException(
            status_code=404,
            detail="Batch not found"
        )

    return updated_batch


@router.delete("/{batch_id}")
def delete_batch_api(batch_id: str):
    deleted = delete_batch(batch_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Batch not found"
        )

    return {
        "message": "Batch deleted successfully"
    }