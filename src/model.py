from ultralytics import YOLO

def load_model(model_path):
  """Load a trained YOLO model from the specified weights file."""
  
  model = YOLO(model_path)
  return model
