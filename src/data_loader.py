from pathlib import Path
def get_dataset_paths(dataset_dir):
"""return paths to the train, valid and test folders"""
  dataset_dir = Path(dataset_dir)
  
  train = dataset_dir / "train"
  valid = dataset_dir / "valid"
  test = dataset_dir / "test"
  
  return {
    "train": train,
    "valid": valid,
    "test": test
  }


def count_images(image_dir):
"""count image files in a directory"""
  image_dir = Path(image_dir)
  
  if not image_dir.is_dir():
    raise FileNotFoundError("Image directory does not exist")
    
  image_extensions = [".jpg", ".jpeg", ".png"]
  
  count = 0
  for file in image_dir.iterdir():
    if file.is_file() and file.suffix.lower() in image_extensions:
      count += 1
      
  return count
