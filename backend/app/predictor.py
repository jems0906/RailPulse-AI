import pandas as pd

from app.model_loader import load_model
from app.explainer import explain_prediction
from app.schemas import EtaRequest

FEATURES = ["distance_miles", "route_segments", "interchanges", "commodity_code", "customer_class_code", "priority_code", "departure_hour", "day_of_week", "month", "season_code", "train_priority", "railcars", "tonnage", "origin_delay_rate", "destination_delay_rate", "historical_transit_hours", "route_on_time_rate"]

def predict_eta(request: EtaRequest) -> dict:
    regressor = load_model("xgb_eta_model.joblib")
    classifier = load_model("xgb_classifier.joblib")
    values = request.model_dump()
    if regressor and classifier:
        frame = pd.DataFrame([{feature: values[feature] for feature in FEATURES}])
        delay = float(regressor.predict(frame)[0])
        probability = max(0.04, min(0.98, float(classifier.predict_proba(frame)[0][0])))
        risk = "high" if probability < 0.62 else "medium" if probability < 0.82 else "low"
        factors = explain_prediction(frame, frame.iloc[0].tolist())
        return {"predicted_delay_hours": round(max(0.1, delay), 2), "on_time_probability": round(probability, 3), "risk_level": risk, "contributing_factors": factors, "model_version": "xgboost-v1"}
    delay = 1.1 + request.distance_miles / 900 + request.interchanges * 1.35
    delay += request.route_segments * 0.07 + request.commodity_code * 0.06 + request.priority_code * 0.08
    delay += (request.origin_delay_rate + request.destination_delay_rate) * 2
    delay += 0.9 if request.priority == "Expedited" else 0
    delay += 0.7 if request.departure_hour in range(16, 22) else 0
    delay = round(max(0.2, delay - (request.train_priority - 1) * 0.65), 2)
    probability = round(max(0.04, min(0.98, 1 - delay / 16)), 3)
    risk = "high" if probability < 0.62 else "medium" if probability < 0.82 else "low"
    factors = [
        {"feature": "Interchanges", "impact": round(request.interchanges * 0.72, 2), "direction": "up"},
        {"feature": "Destination yard delay rate", "impact": round(request.destination_delay_rate * 4.1, 2), "direction": "up"},
        {"feature": "Route distance", "impact": round(request.distance_miles / 700, 2), "direction": "up"},
        {"feature": "Train priority", "impact": round((request.train_priority - 2) * 0.6, 2), "direction": "down" if request.train_priority > 1 else "up"},
    ]
    return {"predicted_delay_hours": delay, "on_time_probability": probability, "risk_level": risk, "contributing_factors": factors, "model_version": "heuristic-v1 (replace with trained artifact)"}
