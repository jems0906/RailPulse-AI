from typing import TypedDict

class NetworkHealth(TypedDict):
    on_time_percentage: float
    active_anomalies: int
    average_delay_hours: float
    high_risk_shipments: int
