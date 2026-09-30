from functools import lru_cache
import joblib
from app.config import MODEL_DIR

@lru_cache
def load_model(name: str):
    path = MODEL_DIR / name
    return joblib.load(path) if path.exists() else None
