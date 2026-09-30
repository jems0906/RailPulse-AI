# Feature engineering guide

The training frame combines route, temporal, yard, and operating signals. `distance_miles`, `interchanges`, and `departure_hour` capture corridor and schedule pressure. Yard delay rates represent historical operating conditions. `train_priority`, `railcars`, and `tonnage` represent the current operating plan.

The same ordered feature list is used by `training/feature_builder.py`, XGBoost training, and FastAPI serving so inference cannot silently reorder model inputs.