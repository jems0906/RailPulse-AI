from xgboost import XGBClassifier

DELAY_THRESHOLD_HOURS = 0.25

def train_classifier(x_train, y_train):
    labels = (y_train > DELAY_THRESHOLD_HOURS).astype(int)
    return XGBClassifier(n_estimators=160, max_depth=4, learning_rate=0.05, subsample=0.85, colsample_bytree=0.85, eval_metric="logloss", random_state=42, n_jobs=2).fit(x_train, labels)
