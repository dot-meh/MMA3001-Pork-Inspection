
import pytest
from src.evaluation import evaluate_model


class DummyModel:
    """A simple substitute for a YOLO model during testing."""

    def val(self, **kwargs):
        return kwargs


def test_evaluate_model_uses_validation_split():
    model = DummyModel()

    result = evaluate_model(model, "data.yaml", split="val")

    assert result["split"] == "val"
    assert result["imgsz"] == 640
    assert result["conf"] == 0.001
    assert result["iou"] == 0.6


def test_evaluate_model_uses_test_split():
    model = DummyModel()

    result = evaluate_model(model, "data.yaml", split="test")

    assert result["split"] == "test"
    assert result["conf"] == 0.001
    assert result["iou"] == 0.6


def test_evaluate_model_rejects_invalid_split():
    model = DummyModel()

    with pytest.raises(ValueError):
        evaluate_model(model, "data.yaml", split="train")
