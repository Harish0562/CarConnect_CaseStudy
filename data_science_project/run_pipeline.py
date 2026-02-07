from __future__ import annotations

import json

from src.data_generation import main as generate_data
from src.evaluate import evaluate_model
from src.train import train_model


def run_pipeline() -> None:
    generated_path = generate_data()
    metrics = train_model(generated_path)
    evaluation = evaluate_model(input_path=generated_path)

    summary = {
        "training_metrics": metrics,
        "evaluation_metrics": evaluation,
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    run_pipeline()
