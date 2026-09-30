from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_session
from app.models import AnomalyAlert, Prediction

router = APIRouter(tags=["history"])

@router.get("/history/predictions")
def prediction_history(session: Session = Depends(get_session)) -> list[dict]:
    rows = session.scalars(select(Prediction).order_by(Prediction.created_at.desc()).limit(50)).all()
    return [{"id": row.id, "origin_yard": row.origin_yard, "destination_yard": row.destination_yard, "predicted_delay_hours": row.predicted_delay_hours, "on_time_probability": row.on_time_probability, "risk_level": row.risk_level, "model_version": row.model_version, "created_at": row.created_at.isoformat()} for row in rows]

@router.get("/history/anomalies")
def anomaly_history(session: Session = Depends(get_session)) -> list[dict]:
    rows = session.scalars(select(AnomalyAlert).order_by(AnomalyAlert.created_at.desc()).limit(50)).all()
    return [{"id": row.id, "yard_id": row.yard_id, "anomaly_score": row.anomaly_score, "is_anomaly": row.is_anomaly, "severity": row.severity, "explanation": row.explanation, "created_at": row.created_at.isoformat()} for row in rows]
