from pathlib import Path
import json
import joblib
from sklearn.model_selection import train_test_split
from training.data_loader import generate_shipments
from training.feature_builder import build_features
from training.evaluate import evaluate_models
from training.train_anomaly_model import train_anomaly_model
from training.train_classifier import train_classifier
from training.train_eta_model import train_eta_models


def train(output_dir: str = "backend/trained_models") -> dict:
    frame = generate_shipments()
    features, target = build_features(frame)
    x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    eta_models = train_eta_models(x_train, y_train)
    classifier = train_classifier(x_train, y_train)
    anomaly = train_anomaly_model(frame)
    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    joblib.dump(eta_models["xgboost"], destination / "xgb_eta_model.joblib")
    joblib.dump(classifier, destination / "xgb_classifier.joblib")
    joblib.dump(anomaly, destination / "isolation_forest.joblib")
    metrics = {**evaluate_models(eta_models, x_test, y_test, classifier), "model": "xgboost", "dataset_rows": len(frame), "training_date": "2026-09-30", "feature_importance": [{"feature": name, "importance": float(value)} for name, value in zip(features.columns, eta_models["xgboost"].feature_importances_)]}
    (destination / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    return metrics

if __name__ == "__main__":
    print(train())
