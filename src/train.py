import argparse
from ultralytics import YOLO

def train_model(data_config, model_weights, output_dir,
                image_size=640, batch_size=16, epochs=50, device=0):
   """
    Train a YOLO object detection model.

    Args:
        data_config (str or Path): Path to the dataset YAML configuration.
        model_weights (str or Path): Path to the initial model weights.
        output_dir (str or Path): Directory for saving training results.
        image_size (int): Input image resolution in pixels.
        batch_size (int): Number of images per training batch.
        epochs (int): Maximum number of training epochs.
        device (int or str): Computing device used for training.

    Returns:
        Results: Training results returned by Ultralytics.
    """

    model = YOLO(model_weights)

    results = model.train(
        data=str(data_config),
        imgsz=image_size,
        batch=batch_size,
        epochs=epochs,
        patience=10,
        seed=42,
        device=device,
        project=str(output_dir),
        name="training_run",
        plots=True
    )

    return results

def parse_arguments():
    """Read training parameters from the command line."""

    parser = argparse.ArgumentParser(
        description="Train a YOLO object detection model"
    )

    parser.add_argument("--data", default="data.yaml")
    parser.add_argument("--weights", default="yolov8n.pt")
    parser.add_argument("--output", default="results")
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--batch", type=int, default=16)
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--device", default="0")
  
    return parser.parse_args()


if __name__ == "__main__":

    args = parse_arguments()

    train_model(
        data_config=args.data,
        model_weights=args.weights,
        output_dir=args.output,
        image_size=args.imgsz,
        batch_size=args.batch,
        epochs=args.epochs,
        device=args.device
    )
