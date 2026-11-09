from ultralytics import YOLO


def load_model(model_path):
    """
    Load a YOLO model from a specified weights file.

    Args:
        model_path (str or Path): Path to the model weights file.

    Returns:
        YOLO: Loaded YOLO model object.
    """

    model = YOLO(model_path)

    return model
