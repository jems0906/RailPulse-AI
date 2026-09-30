import pandas as pd
from sklearn.ensemble import IsolationForest

def build_anomaly_features(frame: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({"dwell_hours": frame["delay_hours"] * 3.2, "scan_gap_hours": frame["interchanges"] * 2.4 + 1, "delay_hours": frame["delay_hours"], "throughput": frame["railcars"] * 4})

def train_anomaly_model(frame: pd.DataFrame):
    return IsolationForest(contamination=0.08, random_state=42).fit(build_anomaly_features(frame))
