def evaluate_model(model, data_config, split="val", imgsz=640):
  """
  Evaluate a YOLO model on a specified data split
  
  Parameters:
    model: Loaded YOLO model
    data_config: Path to the dataset YAML configuration
    split: Dataset split to evaluate
    imgsz: Image size used for evaluation

  Reurns:
    Evaluation results from Ultralytics
  """

  results = model.val(
    data=str(data_config),
    split=split,
    imgsz=imgsz
  )

  return results
