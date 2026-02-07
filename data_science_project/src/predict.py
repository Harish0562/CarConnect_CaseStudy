from __future__ import annotations

import json
from pathlib import Path

import joblib
import pandas as pd

from .config import PATHS
from .data_validation import enforce_types
from .features import build_features


def predict_price(input_path: Path, output_path: Path | None = None) -> Path:
    output_path = output_path or PATHS.data_processed / "price_predictions.csv"
    PATHS.data_processed.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(input_path)
    df = enforce_types(df)
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

    model = joblib.load(PATHS.models / "pricing_model.joblib")
    df["predicted_price"] = model.predict(df[feature_columns])
    df.to_csv(output_path, index=False)

    return output_path


if __name__ == "__main__":
    sample_path = PATHS.data_raw / "rental_demand.csv"
    output = predict_price(sample_path)
    print(json.dumps({"predictions_path": str(output)}, indent=2))
