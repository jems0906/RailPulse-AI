from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_session
from app.models import Prediction
from app.ml.predictor import predict_eta
from app.schemas import EtaRequest, PredictionResponse

router = APIRouter(tags=["predictions"])

@router.post("/predict-eta", response_model=PredictionResponse)
def predict(request: EtaRequest, session: Session = Depends(get_session)) -> dict:
    result = predict_eta(request)
    session.add(Prediction(origin_yard=request.origin_yard, destination_yard=request.destination_yard, predicted_delay_hours=result["predicted_delay_hours"], on_time_probability=result["on_time_probability"], risk_level=result["risk_level"], model_version=result["model_version"]))
    session.commit()
    return result
