from unittest.mock import patch
from src.model import load_model


def test_load_model():
    with patch("src.model.YOLO") as mock_yolo:
        load_model("best.pt")

        mock_yolo.assert_called_once_with("best.pt")
