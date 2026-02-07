import pandas as pd


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["day_of_week"] = df["date"].dt.dayofweek
    df["month"] = df["date"].dt.month
    df["is_peak_season"] = df["month"].isin([6, 7, 8, 12]).astype(int)
    df["lead_time_bucket"] = pd.cut(
        df["lead_time_days"],
        bins=[0, 3, 7, 14, 30],
        labels=["last_minute", "short", "mid", "long"],
        include_lowest=True,
    )
    df["utilization_ratio"] = df["demand"] / df["availability"].clip(lower=1)
    return df
