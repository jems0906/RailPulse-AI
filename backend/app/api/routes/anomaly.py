from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.ml.anomaly_detector import detect_anomaly
from app.db import get_session
from app.models import AnomalyAlert
from app.schemas import AnomalyRequest, AnomalyResponse

router = APIRouter(tags=["anomalies"])

@router.post("/detect-anomaly", response_model=AnomalyResponse)
def anomaly(request: AnomalyRequest, session: Session = Depends(get_session)) -> dict:
    result = detect_anomaly(request)
    session.add(AnomalyAlert(yard_id=request.yard_id, anomaly_score=result["anomaly_score"], is_anomaly=result["is_anomaly"], severity=result["severity"], explanation=result["explanation"]))
    session.commit()
    return result

@router.get("/anomalies")
def alerts() -> list[dict]:
    from app.data import ALERTS
    return ALERTS
