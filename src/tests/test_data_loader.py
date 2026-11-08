from pathlib import Path
from src.data_loader import get_dataset_paths, count_images

def test_get_dataset_paths():
  
  paths = get_dataset_paths("dataset")
  assert paths["train"] == Path("dataset/train")
  assert paths["valid"] == Path("dataset/valid")
  assert paths["test"] == Path("dataset/test")

def test_count_images(tmp_path):
    (tmp_path / "image1.jpg").touch()
    (tmp_path / "image2.png").touch()
    (tmp_path / "notes.txt").touch()

    assert count_images(tmp_path) == 2
