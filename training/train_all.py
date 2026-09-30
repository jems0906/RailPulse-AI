from pathlib import Path
import joblib
import pandas as pd
import json
from sklearn.ensemble import RandomForestRegressor, IsolationForest
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, roc_auc_score, f1_score
from xgboost import XGBClassifier, XGBRegressor
from training.data_loader import generate_shipments
from training.feature_builder import build_features


def train(output_dir: str = "backend/trained_models") -> dict:
    frame = generate_shipments()
    features, target = build_features(frame)
    x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    delayed_train = (y_train > 0.25).astype(int)
    delayed_test = (y_test > 0.25).astype(int)
    linear = LinearRegression().fit(x_train, y_train)
    random_forest = RandomForestRegressor(n_estimators=120, random_state=42, n_jobs=2).fit(x_train, y_train)
    regressor = XGBRegressor(n_estimators=180, max_depth=4, learning_rate=0.05, subsample=0.85, colsample_bytree=0.85, objective="reg:squarederror", random_state=42, n_jobs=2).fit(x_train, y_train)
    classifier = XGBClassifier(n_estimators=160, max_depth=4, learning_rate=0.05, subsample=0.85, colsample_bytree=0.85, eval_metric="logloss", random_state=42, n_jobs=2).fit(x_train, delayed_train)
    anomaly_features = pd.DataFrame({"dwell_hours": frame["delay_hours"] * 3.2, "scan_gap_hours": frame["interchanges"] * 2.4 + 1, "delay_hours": frame["delay_hours"], "throughput": frame["railcars"] * 4})
    anomaly = IsolationForest(contamination=0.08, random_state=42).fit(anomaly_features)
    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    joblib.dump(regressor, destination / "xgb_eta_model.joblib")
    joblib.dump(classifier, destination / "xgb_classifier.joblib")
    joblib.dump(anomaly, destination / "isolation_forest.joblib")
    predictions = regressor.predict(x_test)
    probabilities = classifier.predict_proba(x_test)[:, 1]
    comparison = {"linear_regression_rmse": mean_squared_error(y_test, linear.predict(x_test)) ** 0.5, "random_forest_rmse": mean_squared_error(y_test, random_forest.predict(x_test)) ** 0.5, "xgboost_rmse": mean_squared_error(y_test, predictions) ** 0.5}
    metrics = {**comparison, "auc": roc_auc_score(delayed_test, probabilities), "f1": f1_score(delayed_test, probabilities > 0.5), "model": "xgboost", "dataset_rows": len(frame), "training_date": "2026-09-30", "feature_importance": [{"feature": name, "importance": float(value)} for name, value in zip(features.columns, regressor.feature_importances_)]}
    (destination / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    return metrics

if __name__ == "__main__":
    print(train())
