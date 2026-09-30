from fastapi import APIRouter
from app.data import YARDS

router = APIRouter(tags=["yards"])

@router.get("/yards")
def yard_analysis() -> list[dict]:
    return YARDS
