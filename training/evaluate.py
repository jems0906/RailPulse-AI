from sklearn.metrics import f1_score, mean_squared_error, roc_auc_score

DELAY_THRESHOLD_HOURS = 0.25

def evaluate_models(models, x_test, y_test, classifier) -> dict:
    delayed = (y_test > DELAY_THRESHOLD_HOURS).astype(int)
    probabilities = classifier.predict_proba(x_test)[:, 1]
    return {"linear_regression_rmse": mean_squared_error(y_test, models["linear_regression"].predict(x_test)) ** 0.5, "random_forest_rmse": mean_squared_error(y_test, models["random_forest"].predict(x_test)) ** 0.5, "xgboost_rmse": mean_squared_error(y_test, models["xgboost"].predict(x_test)) ** 0.5, "auc": roc_auc_score(delayed, probabilities), "f1": f1_score(delayed, probabilities > 0.5)}
