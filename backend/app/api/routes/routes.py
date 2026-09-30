from fastapi import APIRouter, HTTPException
from app.data import ROUTES

router = APIRouter(tags=["routes"])

@router.get("/routes")
def route_analysis() -> list[dict]:
    return ROUTES

@router.get("/routes/{origin}/{destination}")
def route_detail(origin: str, destination: str) -> dict:
    for route in ROUTES:
        if route["origin"].lower() == origin.lower() and route["destination"].lower() == destination.lower():
            return route
    raise HTTPException(status_code=404, detail="Route not found")
