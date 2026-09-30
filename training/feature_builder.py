import pandas as pd

FEATURES = ["distance_miles", "route_segments", "interchanges", "commodity_code", "customer_class_code", "priority_code", "departure_hour", "day_of_week", "month", "season_code", "train_priority", "railcars", "tonnage", "origin_delay_rate", "destination_delay_rate", "historical_transit_hours", "route_on_time_rate"]

def build_features(frame: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    features = frame[FEATURES].copy()
    target = frame["delay_hours"]
    return features, target
