from pydantic import BaseModel, Field

class EtaRequest(BaseModel):
    origin_yard: str = "Alliance"
    destination_yard: str = "Chicago"
    commodity: str = "Agriculture"
    priority: str = "Standard"
    customer_class: str = "Contract"
    distance_miles: float = Field(780, ge=1)
    route_segments: int = Field(7, ge=1)
    interchanges: int = Field(1, ge=0)
    commodity_code: int = Field(1, ge=0, le=4)
    customer_class_code: int = Field(1, ge=0, le=3)
    priority_code: int = Field(1, ge=0, le=2)
    departure_hour: int = Field(8, ge=0, le=23)
    day_of_week: int = Field(2, ge=0, le=6)
    month: int = Field(9, ge=1, le=12)
    season_code: int = Field(3, ge=1, le=4)
    train_priority: int = Field(2, ge=1, le=3)
    railcars: int = Field(90, ge=1)
    tonnage: float = Field(9000, ge=1)
    origin_delay_rate: float = Field(0.08, ge=0, le=1)
    destination_delay_rate: float = Field(0.12, ge=0, le=1)
    historical_transit_hours: float = Field(24, ge=0)
    route_on_time_rate: float = Field(0.86, ge=0, le=1)

class AnomalyRequest(BaseModel):
    yard_id: str = "Alliance"
    dwell_hours: float = Field(18, ge=0)
    scan_gap_hours: float = Field(6, ge=0)
    delay_hours: float = Field(3, ge=0)
    throughput: float = Field(420, ge=0)

class PredictionResponse(BaseModel):
    predicted_delay_hours: float
    on_time_probability: float
    risk_level: str
    contributing_factors: list[dict[str, object]]
    model_version: str

class AnomalyResponse(BaseModel):
    anomaly_score: float
    is_anomaly: bool
    severity: str
    explanation: str
