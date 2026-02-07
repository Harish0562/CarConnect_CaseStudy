from pathlib import Path

import numpy as np
import pandas as pd

from .config import PATHS


def _seasonality_index(day_of_year: int) -> float:
    return 1.0 + 0.3 * np.sin(2 * np.pi * day_of_year / 365)


def generate_synthetic_rentals(
    start_date: str = "2022-01-01",
    end_date: str = "2024-12-31",
    seed: int = 42,
) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="D")

    vehicle_classes = ["economy", "compact", "midsize", "suv", "luxury"]
    base_demand = {
        "economy": 45,
        "compact": 38,
        "midsize": 30,
        "suv": 25,
        "luxury": 12,
    }
    base_price = {
        "economy": 35,
        "compact": 45,
        "midsize": 55,
        "suv": 75,
        "luxury": 120,
    }

    rows = []
    for date in dates:
        day_of_year = date.timetuple().tm_yday
        seasonality = _seasonality_index(day_of_year)
        weekend = int(date.weekday() >= 5)
        holiday = int(date.month == 12 and date.day in {24, 25, 31})
        local_event = int(rng.random() < 0.08)

        for vehicle_class in vehicle_classes:
            lead_time = rng.integers(1, 30)
            duration = rng.integers(1, 14)
            availability = rng.integers(20, 120)
            competitor_price = base_price[vehicle_class] * rng.normal(1.0, 0.08)

            demand = (
                base_demand[vehicle_class]
                * seasonality
                * (1.15 if weekend else 0.9)
                * (1.2 if holiday else 1.0)
                * (1.1 if local_event else 1.0)
                * rng.normal(1.0, 0.15)
            )
            demand = max(0, demand)

            dynamic_price = (
                base_price[vehicle_class]
                * (1.2 if weekend else 1.0)
                * (1.25 if holiday else 1.0)
                * (1.15 if local_event else 1.0)
                * (1 + 0.3 * (demand / (availability + 1)))
                * rng.normal(1.0, 0.05)
            )

            rows.append(
                {
                    "date": date,
                    "vehicle_class": vehicle_class,
                    "lead_time_days": lead_time,
                    "rental_duration_days": duration,
                    "availability": availability,
                    "competitor_price": round(competitor_price, 2),
                    "weekend": weekend,
                    "holiday": holiday,
                    "local_event": local_event,
                    "seasonality_index": round(seasonality, 3),
                    "demand": round(demand, 2),
                    "price": round(dynamic_price, 2),
                }
            )

    return pd.DataFrame(rows)


def main() -> Path:
    PATHS.data_raw.mkdir(parents=True, exist_ok=True)
    output_path = PATHS.data_raw / "rental_demand.csv"
    df = generate_synthetic_rentals()
    df.to_csv(output_path, index=False)
    return output_path


if __name__ == "__main__":
    generated = main()
    print(f"Generated dataset at {generated}")
