from __future__ import annotations

import pandas as pd


REQUIRED_COLUMNS = {
    "date",
    "vehicle_class",
    "lead_time_days",
    "rental_duration_days",
    "availability",
    "competitor_price",
    "weekend",
    "holiday",
    "local_event",
    "seasonality_index",
    "demand",
    "price",
}


def validate_schema(df: pd.DataFrame) -> list[str]:
    errors = []
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        errors.append(f"Missing required columns: {sorted(missing)}")

    if (df["availability"] <= 0).any():
        errors.append("Availability must be positive.")
    if (df["price"] <= 0).any():
        errors.append("Price must be positive.")
    if (df["rental_duration_days"] <= 0).any():
        errors.append("Rental duration must be positive.")

    return errors


def enforce_types(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    categorical_columns = ["vehicle_class"]
    for column in categorical_columns:
        df[column] = df[column].astype("category")
    return df


def validate_and_clean(df: pd.DataFrame) -> pd.DataFrame:
    df = enforce_types(df)
    errors = validate_schema(df)
    if errors:
        raise ValueError("; ".join(errors))
    return df
