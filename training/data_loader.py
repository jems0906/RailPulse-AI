from pathlib import Path
import numpy as np
import pandas as pd


def generate_shipments(rows: int = 5000, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    distance = rng.integers(180, 1100, rows)
    route_segments = np.maximum(2, (distance / 120).astype(int) + rng.integers(0, 3, rows))
    interchanges = rng.integers(0, 3, rows)
    commodity_code = rng.integers(0, 5, rows)
    customer_class_code = rng.integers(0, 4, rows)
    priority_code = rng.integers(0, 3, rows)
    departure_hour = rng.integers(0, 24, rows)
    day_of_week = rng.integers(0, 7, rows)
    month = rng.integers(1, 13, rows)
    season_code = ((month % 12) // 3) + 1
    origin_rate = rng.uniform(0.04, 0.2, rows)
    destination_rate = rng.uniform(0.04, 0.22, rows)
    train_priority = rng.integers(1, 4, rows)
    railcars = rng.integers(40, 150, rows)
    tonnage = rng.uniform(4000, 16000, rows)
    historical_transit = distance / 38 + route_segments * 0.4 + rng.normal(0, 1.2, rows)
    route_on_time = np.clip(0.98 - interchanges * 0.08 - (origin_rate + destination_rate) * 0.45, 0.35, 0.98)
    delay = 0.01 + distance / 2200 + route_segments * 0.03 + interchanges * 0.22 + commodity_code * 0.04 + priority_code * 0.04 + (origin_rate + destination_rate) * 0.6 + rng.normal(0, 0.25, rows)
    frame = pd.DataFrame({"distance_miles": distance, "route_segments": route_segments, "interchanges": interchanges, "commodity_code": commodity_code, "customer_class_code": customer_class_code, "priority_code": priority_code, "departure_hour": departure_hour, "day_of_week": day_of_week, "month": month, "season_code": season_code, "train_priority": train_priority, "railcars": railcars, "tonnage": tonnage, "origin_delay_rate": origin_rate, "destination_delay_rate": destination_rate, "historical_transit_hours": historical_transit, "route_on_time_rate": route_on_time, "delay_hours": np.maximum(delay, 0.01)})
    frame["delayed"] = (frame["delay_hours"] > 0.25).astype(int)
    return frame

def save_samples(output_dir: str = "data_samples") -> None:
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    shipments = generate_shipments()
    shipments.to_csv(path / "shipments.csv", index=False)
    yards = pd.DataFrame([{ "yard_id": "Alliance", "region": "Plains", "average_daily_throughput": 520, "historical_delay_rate": 0.08 }, { "yard_id": "Chicago", "region": "Midwest", "average_daily_throughput": 680, "historical_delay_rate": 0.14 }, { "yard_id": "Kansas City", "region": "Plains", "average_daily_throughput": 590, "historical_delay_rate": 0.11 }, { "yard_id": "Fort Worth", "region": "South", "average_daily_throughput": 630, "historical_delay_rate": 0.09 }, { "yard_id": "Memphis", "region": "South", "average_daily_throughput": 410, "historical_delay_rate": 0.17 }, { "yard_id": "Omaha", "region": "Plains", "average_daily_throughput": 460, "historical_delay_rate": 0.07 }])
    yards.to_csv(path / "yards.csv", index=False)
    routes = pd.DataFrame([{ "route_id": "R-001", "origin_yard": "Alliance", "destination_yard": "Chicago", "distance_miles": 780, "route_segments": 7, "interchanges": 1 }, { "route_id": "R-002", "origin_yard": "Omaha", "destination_yard": "Memphis", "distance_miles": 690, "route_segments": 6, "interchanges": 2 }, { "route_id": "R-003", "origin_yard": "Fort Worth", "destination_yard": "Kansas City", "distance_miles": 510, "route_segments": 5, "interchanges": 1 }])
    routes.to_csv(path / "routes.csv", index=False)
    trains = pd.DataFrame({"train_id": ["BNSF-401", "BNSF-612", "BNSF-887"], "train_priority": [1, 2, 3], "scheduled_departure": ["2026-09-30T06:00:00Z", "2026-09-30T08:00:00Z", "2026-09-30T11:00:00Z"], "railcars": [108, 92, 74], "total_tonnage": [14200, 9800, 7200]})
    trains.to_csv(path / "trains.csv", index=False)
    events = pd.DataFrame({"event_id": range(1, 7), "train_id": ["BNSF-401", "BNSF-401", "BNSF-612", "BNSF-612", "BNSF-887", "BNSF-887"], "yard_id": ["Alliance", "Chicago", "Omaha", "Memphis", "Fort Worth", "Kansas City"], "event_type": ["departure", "arrival", "departure", "arrival", "departure", "arrival"], "dwell_hours": [8.2, 16.4, 11.1, 21.2, 7.4, 12.6]})
    events.to_csv(path / "scan_events.csv", index=False)
