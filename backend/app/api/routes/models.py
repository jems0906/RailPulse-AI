from fastapi import APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["models"])

@router.get("/models/performance")
def performance() -> dict:
    metrics_path = Path(__file__).resolve().parents[3] / "trained_models" / "metrics.json"
    if metrics_path.exists():
        metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
        return {"models": [{"name": "Linear Regression", "type": "baseline", "rmse_hours": metrics["linear_regression_rmse"], "status": "comparison"}, {"name": "Random Forest", "type": "comparison", "rmse_hours": metrics["random_forest_rmse"], "status": "comparison"}, {"name": "XGBoost ETA Regressor", "type": "regression", "rmse_hours": metrics["xgboost_rmse"], "status": "production"}, {"name": "XGBoost On-time Classifier", "type": "classification", "auc": metrics["auc"], "f1": metrics["f1"], "status": "production"}, {"name": "Isolation Forest", "type": "anomaly", "status": "production"}], "feature_importance": metrics["feature_importance"], "training_date": metrics["training_date"], "dataset_rows": metrics["dataset_rows"]}
    return {"models": [], "feature_importance": [], "training_date": None, "dataset_rows": 0}
