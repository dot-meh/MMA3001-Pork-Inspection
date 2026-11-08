from pathlib import path
def get_dataset_paths(dataset_dir):
  dataset_dir = Path(dataset_dir)
  
  train = dataset_dir / "train"
  valid = dataset_dir / "valid"
  test = dataset_dir / "test"
  
  return {
    "train": train,
    "valid": valid,
    "test": test
  }
