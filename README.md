# MLOps with MLflow

Track experiments, log metrics and artifacts, and register models with [MLflow](https://mlflow.org/). Set up for local development and optional remote tracking server.

## Features

- **Experiment tracking** — log params, metrics, and artifacts per run
- **Model registry** — register and promote models to staging/production
- **Reproducibility** — conda/env and code versioning
- **Minimal training script** — example `train.py` with MLflow logging

## Requirements

- Python 3.10+
- MLflow 2.x

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

- Default: local artifact and backend under `./mlruns`
- Remote: set `MLFLOW_TRACKING_URI` and (optional) artifact store (S3, GCS, etc.)

## Usage

Run a training run (logs to MLflow):

```bash
python train.py
```

Start the MLflow UI to compare runs:

```bash
mlflow ui --backend-store-uri ./mlruns
```

## License

MIT
