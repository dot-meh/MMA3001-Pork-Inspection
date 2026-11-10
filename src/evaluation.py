def evaluate_model(model, data_config, split="val", imgsz=640):
    """
    Evaluate a YOLO model on a specified dataset split.

    Args:
        model: Loaded Ultralytics YOLO model.
        data_config (str or Path): Path to the dataset YAML configuration.
        split (str): Dataset split to evaluate ('val' or 'test').
        imgsz (int): Image resolution used during evaluation.

    Returns:
        Results: Evaluation results returned by Ultralytics.

    Raises:
        ValueError: If split is not 'val' or 'test'.
    """

    if split not in ["val", "test"]:
        raise ValueError("split must be either 'val' or 'test'")

    results = model.val(
        data=str(data_config),
        split=split,
        imgsz=imgsz,
        conf = 0.001,
        iou = 0.6
    )

    return results
