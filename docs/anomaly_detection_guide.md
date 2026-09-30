# Anomaly detection guide

Isolation Forest is trained on synthetic dwell hours, scan gap hours, delay hours, and throughput. The API returns a normalized anomaly score, boolean flag, severity, and plain-language explanation. In production, retrain the baseline by corridor and season and monitor false positives with dispatcher feedback.