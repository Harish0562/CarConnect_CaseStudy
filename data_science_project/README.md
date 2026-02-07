# CarConnect Demand Forecasting & Dynamic Pricing (End-to-End DS Project)

## Why this project matters
Car rental revenue is driven by **matching supply with demand** while setting **optimal prices**. This project simulates a realistic rental environment and delivers a production-grade, end-to-end data science workflow you can showcase in interviews:

- **Business problem:** Predict daily demand and rental price to maximize revenue and reduce idle inventory.
- **Outcome:** A reproducible ML pipeline that generates data, validates it, engineers features, trains a model, and produces evaluation artifacts.

## Project highlights
- **End-to-end ML pipeline** with clear stages (generation → validation → feature engineering → training → evaluation).
- **Robust feature engineering** (seasonality, lead time, availability constraints, vehicle class, holiday/weekend effects).
- **Modeling** with a modern scikit-learn pipeline (preprocessing + estimator).
- **Repeatable runs** using a single command.

## Architecture
```
root/
  data_science_project/
    data/
      raw/
      processed/
    models/
    src/
      config.py
      data_generation.py
      data_validation.py
      features.py
      train.py
      evaluate.py
      predict.py
    run_pipeline.py
    requirements.txt
```

## How to run
```bash
pip install -r data_science_project/requirements.txt
python data_science_project/run_pipeline.py
```

Artifacts are saved under:
- `data/raw/` and `data/processed/`
- `models/` (trained model + metrics)

## Example use-cases you can discuss
- **Capacity planning:** Forecast daily demand per vehicle class.
- **Dynamic pricing:** Estimate price elasticity to maximize revenue.
- **Inventory optimization:** Predict future utilization to inform fleet sizing.

## Next steps (optional)
- Replace synthetic data with production data sources.
- Add model monitoring (data drift + performance decay alerts).
- Deploy via FastAPI + Docker, or schedule with Airflow.
