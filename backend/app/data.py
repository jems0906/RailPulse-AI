from datetime import datetime, timedelta

YARDS = [
    {"id": "Alliance", "region": "Plains", "throughput": 520, "delay_rate": 0.08, "dwell": 11.4},
    {"id": "Chicago", "region": "Midwest", "throughput": 680, "delay_rate": 0.14, "dwell": 16.8},
    {"id": "Kansas City", "region": "Plains", "throughput": 590, "delay_rate": 0.11, "dwell": 13.2},
    {"id": "Fort Worth", "region": "South", "throughput": 630, "delay_rate": 0.09, "dwell": 10.5},
    {"id": "Memphis", "region": "South", "throughput": 410, "delay_rate": 0.17, "dwell": 18.1},
    {"id": "Omaha", "region": "Plains", "throughput": 460, "delay_rate": 0.07, "dwell": 9.8},
]
ROUTES = [
    {"route": "Alliance -> Chicago", "origin": "Alliance", "destination": "Chicago", "delay": 5.8, "risk": 0.31, "trend": [3.2, 4.0, 3.7, 5.1, 5.8, 4.9, 5.8]},
    {"route": "Fort Worth -> Kansas City", "origin": "Fort Worth", "destination": "Kansas City", "delay": 3.1, "risk": 0.18, "trend": [2.4, 2.9, 2.5, 3.7, 3.1, 2.8, 3.1]},
    {"route": "Omaha -> Memphis", "origin": "Omaha", "destination": "Memphis", "delay": 7.4, "risk": 0.46, "trend": [5.2, 5.8, 6.6, 7.1, 6.8, 7.9, 7.4]},
    {"route": "Kansas City -> Fort Worth", "origin": "Kansas City", "destination": "Fort Worth", "delay": 2.2, "risk": 0.12, "trend": [2.5, 2.2, 2.0, 2.6, 2.1, 2.4, 2.2]},
]
ALERTS = [
    {"id": "ALT-1042", "yard": "Chicago", "type": "Dwell spike", "severity": "high", "message": "Average dwell is 41% above the 30-day baseline.", "time": "12 min ago"},
    {"id": "ALT-1041", "yard": "Memphis", "type": "Scan gap", "severity": "medium", "message": "18 railcars have not reported a scan in 9.4 hours.", "time": "34 min ago"},
    {"id": "ALT-1040", "yard": "Alliance", "type": "Corridor congestion", "severity": "low", "message": "Eastbound interchange queue is trending above normal.", "time": "1 hr ago"},
]

def network_health() -> dict:
    return {"on_time_percentage": 87.4, "active_anomalies": 7, "average_delay_hours": 3.8, "high_risk_shipments": 24, "shipments_monitored": 1842, "updated_at": datetime.utcnow().isoformat() + "Z"}

def weekly_summary() -> dict:
    return {"period": "Sep 23 - Sep 29, 2026", "headline": "Network reliability held steady while two Midwest yards experienced elevated dwell.", "insights": ["On-time performance improved 2.1 points week over week.", "Chicago and Memphis account for 62% of active anomaly signals.", "Agriculture shipments show the highest sensitivity to interchange count."], "recommended_actions": ["Review Chicago inbound crew staging before the evening peak.", "Prioritize scan compliance at Memphis for the next operating cycle."]}
