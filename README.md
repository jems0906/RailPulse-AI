# RailPulse AI

RailPulse is an AI-powered rail network intelligence platform for freight ETA risk, operational anomaly detection, and explainable network monitoring.

## Run locally

### Backend

```text
cd backend
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

The API is available at `http://localhost:8000/docs`.

### Frontend

```text
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`. Set `VITE_API_URL` to point the dashboard at a deployed backend.

### Train synthetic models

From the repository root, after installing backend requirements:

```text
python training/train_all.py
```

This writes model artifacts to `backend/trained_models/`. Training is local or CI-only; Railway runs inference. The backend stores prediction and anomaly history using `DATABASE_URL` (SQLite locally, Railway PostgreSQL in deployment).

## Project map

- `backend/app`: FastAPI service, schemas, prediction and anomaly logic
- `training`: synthetic data generation, feature building, model training
- `frontend/src`: React operational dashboard
- `docs`: architecture and model card
- `railway.json`: two-service Railway deployment definition
