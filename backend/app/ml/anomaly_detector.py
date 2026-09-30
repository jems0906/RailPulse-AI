import pandas as pd
from app.schema_types import AnomalyRequest
from app.ml.model_loader import load_model

def detect_anomaly(request: AnomalyRequest) -> dict:
	model = load_model("isolation_forest.joblib")
	if model:
		values = pd.DataFrame([{"dwell_hours": request.dwell_hours, "scan_gap_hours": request.scan_gap_hours, "delay_hours": request.delay_hours, "throughput": request.throughput}])
		raw_score = float(-model.score_samples(values)[0])
		score = min(0.99, max(0.01, raw_score))
		is_anomaly = model.predict(values)[0] == -1
		severity = "high" if score >= 0.65 else "medium" if is_anomaly else "low"
		explanation = "Isolation Forest identified an operating pattern outside the trained baseline." if is_anomaly else "Observed operating values are within the trained baseline range."
		return {"anomaly_score": round(score, 3), "is_anomaly": is_anomaly, "severity": severity, "explanation": explanation}
	score = min(0.99, max(0.01, request.dwell_hours / 42 + request.scan_gap_hours / 36 + request.delay_hours / 22))
	is_anomaly = score >= 0.55
	severity = "critical" if score >= 0.8 else "high" if score >= 0.65 else "medium" if is_anomaly else "low"
	explanation = "Dwell, scan gap, and delay are collectively outside the recent operating baseline." if is_anomaly else "Observed operating values are within the recent baseline range."
	return {"anomaly_score": round(score, 3), "is_anomaly": is_anomaly, "severity": severity, "explanation": explanation}

__all__ = ["detect_anomaly"]
