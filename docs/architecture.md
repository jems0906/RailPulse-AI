# RailPulse AI architecture

RailPulse is a three-service deployment: a React/Vite dashboard, a FastAPI inference API, and Railway-managed PostgreSQL for durable prediction and alert history.

The API creates `predictions` and `anomaly_alerts` tables on startup. Local development defaults to SQLite; Railway uses `DATABASE_URL` with PostgreSQL and the bundled Psycopg driver.

The training pipeline runs locally or in CI. `training/train_all.py` creates the regression, classification, and Isolation Forest artifacts in `backend/trained_models/`. Railway serves inference only; it does not train models. The API currently exposes a deterministic development fallback so the product remains demonstrable before artifacts are generated.

## API surface

- `POST /api/predict-eta`
- `POST /api/detect-anomaly`
- `GET /api/dashboard/network-health`
- `GET /api/dashboard/route-analysis`
- `GET /api/dashboard/yard-analysis`
- `GET /api/dashboard/alerts`
- `GET /api/dashboard/leader-update`
- `GET /api/models/performance`
- `GET /api/history/predictions`
- `GET /api/history/anomalies`
