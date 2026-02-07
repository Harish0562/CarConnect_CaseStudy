from __future__ import annotations

import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from .config import PATHS
from .data_validation import validate_and_clean
from .features import build_features

TARGET_COLUMN = "price"


def evaluate_model(
    model_path: Path | None = None,
    input_path: Path | None = None,
) -> dict[str, float]:
    model_path = model_path or PATHS.models / "pricing_model.joblib"
    input_path = input_path or PATHS.data_raw / "rental_demand.csv"

    df = pd.read_csv(input_path)
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

    model = joblib.load(model_path)
    predictions = model.predict(X)

    metrics = {
        "mae": mean_absolute_error(y, predictions),
        "rmse": mean_squared_error(y, predictions, squared=False),
        "r2": r2_score(y, predictions),
    }

    metrics_path = PATHS.models / "evaluation.json"
    metrics_path.write_text(json.dumps(metrics, indent=2))
    return metrics


if __name__ == "__main__":
    results = evaluate_model()
    print(json.dumps(results, indent=2))
