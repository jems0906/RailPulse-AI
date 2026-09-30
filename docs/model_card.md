# RailPulse model card

## Intended use

Estimate freight shipment delay risk and surface unusual operational conditions for dispatchers and network leaders. Predictions support decisions; they do not replace operating rules or dispatcher judgment.

## Models

The training pipeline compares a Gradient Boosted Regressor for delay hours, a Gradient Boosted Classifier for on-time probability, and an Isolation Forest for anomaly detection. SHAP-style feature contributions are returned by the API contract; the serving fallback provides ranked contributing factors until trained artifacts are present.

## Limitations

The included dataset is synthetic and designed to exercise the product workflow. It does not represent live BNSF data, weather, crew availability, maintenance windows, or embargo conditions. Before production use, calibrate against historical events, validate by corridor and season, monitor drift, and add human review for high-impact decisions.
