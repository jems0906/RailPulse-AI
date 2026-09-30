from app.ml.model_loader import load_model

FEATURE_LABELS = {"distance_miles": "Route distance", "route_segments": "Route segments", "interchanges": "Interchanges", "commodity_code": "Commodity", "customer_class_code": "Customer class", "priority_code": "Priority", "departure_hour": "Departure hour", "day_of_week": "Day of week", "month": "Month", "season_code": "Season", "train_priority": "Train priority", "railcars": "Railcars", "tonnage": "Total tonnage", "origin_delay_rate": "Origin yard delay rate", "destination_delay_rate": "Destination yard delay rate", "historical_transit_hours": "Historical transit time", "route_on_time_rate": "Historical route on-time rate"}

def explain_prediction(frame, values: list[float]) -> list[dict[str, object]]:
	model = load_model("xgb_eta_model.joblib")
	if model is None:
		return []
	try:
		import shap
		explanation = shap.TreeExplainer(model)(frame)
		contributions = explanation.values[0]
		return sorted(({"feature": FEATURE_LABELS.get(name, name), "impact": round(float(value), 3), "direction": "up" if value >= 0 else "down"} for name, value in zip(frame.columns, contributions)), key=lambda item: abs(float(item["impact"])), reverse=True)[:5]
	except Exception:
		return []

__all__ = ["explain_prediction"]
