from __future__ import annotations

import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from .config import PATHS
from .data_validation import validate_and_clean
from .features import build_features

TARGET_COLUMN = "price"


def _train_model(df: pd.DataFrame) -> tuple[Pipeline, dict[str, float]]:
    df = validate_and_clean(df)
    df = build_features(df)

    feature_columns = [
        "vehicle_class",
        "lead_time_days",
        "rental_duration_days",
        "availability",
        "competitor_price",
        "weekend",
        "holiday",
        "local_event",
        "seasonality_index",
        "day_of_week",
        "month",
        "is_peak_season",
        "lead_time_bucket",
        "utilization_ratio",
    ]

    X = df[feature_columns]
    y = df[TARGET_COLUMN]

    categorical_features = ["vehicle_class", "lead_time_bucket"]
    numeric_features = [column for column in feature_columns if column not in categorical_features]

    preprocessor = ColumnTransformer(
        transformers=[
            ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical_features),
            ("numeric", "passthrough", numeric_features),
        ]
    )

    model = HistGradientBoostingRegressor(
        max_depth=6,
        learning_rate=0.08,
        max_iter=250,
        random_state=42,
    )

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    pipeline.fit(X_train, y_train)
    predictions = pipeline.predict(X_test)

    metrics = {
        "mae": mean_absolute_error(y_test, predictions),
        "rmse": mean_squared_error(y_test, predictions, squared=False),
        "r2": r2_score(y_test, predictions),
    }

    return pipeline, metrics


def train_model(input_path: Path | None = None) -> dict[str, float]:
    input_path = input_path or PATHS.data_raw / "rental_demand.csv"
    df = pd.read_csv(input_path)

    pipeline, metrics = _train_model(df)

    PATHS.models.mkdir(parents=True, exist_ok=True)
    model_path = PATHS.models / "pricing_model.joblib"
    metrics_path = PATHS.models / "metrics.json"

    joblib.dump(pipeline, model_path)
    metrics_path.write_text(json.dumps(metrics, indent=2))

    return metrics


if __name__ == "__main__":
    results = train_model()
    print(json.dumps(results, indent=2))
