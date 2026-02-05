"""
Example training script with MLflow logging.
Run: python train.py
"""
try:
    import mlflow
except ImportError:
    mlflow = None


def train_epoch(epoch: int) -> float:
    """Fake training; return loss."""
    return 1.0 / (epoch + 1)


def main():
    if mlflow is None:
        print("Install mlflow: pip install mlflow")
        return
    with mlflow.start_run(run_name="example-run") as run:
        mlflow.log_param("model", "linear")
        mlflow.log_param("epochs", 3)
        for epoch in range(3):
            loss = train_epoch(epoch)
            mlflow.log_metric("loss", loss, step=epoch)
        mlflow.log_artifact(".", artifact_path="code")
    print("Run logged. View with: mlflow ui --backend-store-uri ./mlruns")


if __name__ == "__main__":
    main()
