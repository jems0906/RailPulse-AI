from fastapi import APIRouter
from app.data import ALERTS, network_health, weekly_summary

router = APIRouter(tags=["dashboards"])

@router.get("/dashboard/network-health")
def network() -> dict:
    return network_health()

@router.get("/dashboard/route-analysis")
def route_dashboard() -> list[dict]:
    from app.data import ROUTES
    return ROUTES

@router.get("/dashboard/yard-analysis")
def yard_dashboard() -> list[dict]:
    from app.data import YARDS
    return YARDS

@router.get("/dashboard/alerts")
def alert_dashboard() -> list[dict]:
    return ALERTS

@router.get("/dashboard/leader-update")
def leader_update() -> dict:
    return weekly_summary()
