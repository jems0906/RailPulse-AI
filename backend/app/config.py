from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_DIR = BASE_DIR / "trained_models"
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./railpulse.db")
if DATABASE_URL.startswith("postgresql://"):
	DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg://", 1)
elif DATABASE_URL.startswith("postgres://"):
	DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+psycopg://", 1)
