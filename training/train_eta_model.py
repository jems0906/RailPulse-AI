from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor


def train_eta_models(x_train, y_train):
    return {
        "linear_regression": LinearRegression().fit(x_train, y_train),
        "random_forest": RandomForestRegressor(n_estimators=120, random_state=42, n_jobs=2).fit(x_train, y_train),
        "xgboost": XGBRegressor(n_estimators=180, max_depth=4, learning_rate=0.05, subsample=0.85, colsample_bytree=0.85, objective="reg:squarederror", random_state=42, n_jobs=2).fit(x_train, y_train),
    }
