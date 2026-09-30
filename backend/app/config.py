from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_DIR = BASE_DIR / "trained_models"
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./railpulse.db")
