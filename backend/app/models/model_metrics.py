from dataclasses import dataclass

@dataclass(frozen=True)
class ModelMetrics:
    name: str
    value: float
    metric: str
