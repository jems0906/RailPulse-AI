from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get('/api/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'healthy'

def test_eta_prediction():
    response = client.post('/api/predict-eta', json={'distance_miles': 780, 'interchanges': 1})
    assert response.status_code == 200
    assert response.json()['predicted_delay_hours'] > 0
    assert 0 < response.json()['on_time_probability'] <= 1

def test_anomaly_detection():
    response = client.post('/api/detect-anomaly', json={'dwell_hours': 30, 'scan_gap_hours': 10, 'delay_hours': 8})
    assert response.status_code == 200
    assert response.json()['is_anomaly'] is True

def test_prediction_history_is_persisted():
    response = client.get('/api/history/predictions')
    assert response.status_code == 200
    assert response.json()
    assert response.json()[0]['destination_yard'] == 'Chicago'
