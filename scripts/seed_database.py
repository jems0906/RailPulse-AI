import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.db import SessionLocal, init_db
from app.models import AnomalyAlert, Prediction

if __name__ == "__main__":
    init_db()
    with SessionLocal() as session:
        session.add_all([Prediction(origin_yard="Alliance", destination_yard="Chicago", predicted_delay_hours=5.8, on_time_probability=0.64, risk_level="medium", model_version="xgboost-v1"), Prediction(origin_yard="Omaha", destination_yard="Memphis", predicted_delay_hours=7.4, on_time_probability=0.51, risk_level="high", model_version="xgboost-v1")])
        session.add(AnomalyAlert(yard_id="Chicago", anomaly_score=0.81, is_anomaly=True, severity="high", explanation="Dwell is outside the trained operating baseline."))
        session.commit()
    print("Seeded sample prediction and anomaly history.")