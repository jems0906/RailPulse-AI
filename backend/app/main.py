from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.routes import anomaly, dashboards, health, history, models, predict, routes, yards
from app.db import init_db

app = FastAPI(title="RailPulse AI", version="1.0.0", description="Rail network intelligence API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
init_db()

app.include_router(health.router, prefix="/api")
app.include_router(predict.router, prefix="/api")
app.include_router(anomaly.router, prefix="/api")
app.include_router(routes.router, prefix="/api")
app.include_router(yards.router, prefix="/api")
app.include_router(dashboards.router, prefix="/api")
app.include_router(models.router, prefix="/api")
app.include_router(history.router, prefix="/api")

frontend_dist = Path(__file__).resolve().parents[2] / "frontend_dist"
if frontend_dist.exists():
    app.mount("/", StaticFiles(directory=frontend_dist, html=True), name="frontend")

@app.get("/")
def root() -> dict[str, str]:
    return {"name": "RailPulse AI", "status": "online", "docs": "/docs"}
