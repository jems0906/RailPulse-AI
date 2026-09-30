from datetime import datetime, timezone
from sqlalchemy import DateTime, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base

class Prediction(Base):
    __tablename__ = "predictions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    origin_yard: Mapped[str] = mapped_column(String(80))
    destination_yard: Mapped[str] = mapped_column(String(80))
    predicted_delay_hours: Mapped[float] = mapped_column(Float)
    on_time_probability: Mapped[float] = mapped_column(Float)
    risk_level: Mapped[str] = mapped_column(String(20))
    model_version: Mapped[str] = mapped_column(String(80))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

class AnomalyAlert(Base):
    __tablename__ = "anomaly_alerts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    yard_id: Mapped[str] = mapped_column(String(80))
    anomaly_score: Mapped[float] = mapped_column(Float)
    is_anomaly: Mapped[bool] = mapped_column(default=False)
    severity: Mapped[str] = mapped_column(String(20))
    explanation: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
