# Experimental Log - Pork Rasher Defect Detection

## 1. Project Objective
The project uses YOLO based object detection to automate visual inspection of package pork rashers.
The objective is to identify, classify and localize five possible defect classes.

- Loose meat
- Packing-Errors
- Twisted Meat
- Unsealed Meat
- Wrinkled Meat

## 2. Dataset
Source - RoboFlow - Pork Rasher Error Packaging, Version 4
Dataset Split
- Training: 3349 Images
- Validation: 120 Images
- Training: 80 Images
- Total: 3549 Images

Identified Limitations in Dataset
1. Small validation and training sets
2. Some related source images occur across different dataset splits
3. No wrinkle examples appear in the training or validation sets
4. Some images contain empty annotations

## 3. Experimental Setup

Architecture: YOLOv8
Framework: Ultralytics
Hardware: NVIDIA Tesla T4
Dataset: Roboflow v4
Random Seed: 42
Maximum Epochs: 50
Early stopping patience: 10

Models were evaluated using
- Precision
- Recall
- mAP50
- mAP50 - 95


## 4. Experiments and Results
### 4.1 YOLOv8n
Purpose: Establish Baseline Results

Parameters
Batch size: 16
Image Resolution: 640x640

Metrics/Results
Precision: 0.650
Recall: 0.617
mAP50: 0.623
mAP50-95: 0.348
Inference Time: 4.4ms/image

### 4.2 YOLOv8s - 640px
Purpose: Investigate effect of increasing model complexity

Parameters
Batch size: 16
Image Resolution: 640x640

Metrics/Results
Precision: 0.781
Recall: 0.619
mAP50: 0.681
mAP50-95: 0.424
Inference Time: 7.9ms/image

### 4.3 YOLOv8s - 960px
Purpose: Investigate if higher image resolution improves detection of smaller defects

Parameters
Batch size: 8
Image Resolution: 960x960

Metrics/Results
Precision: 0.700
Recall: 0.681
mAP50: 0.650
mAP50-95: 0.329
Inference Time: 19.6 ms/image

### 4.4 YOLOv8s - 1280px
Purpose: Investigate further increase in image resolution improves small defect detection (specifically packagine errors)

Parameters
Batch size: 4
Image Resolution: 1280x1280

Metrics/Results
Precision: 0.551
Recall: 0.552
mAP50: 0.544
mAP50-95: 0.296
Inference Time: 14.3 ms

Observations
1280px did not improve detection performance compared with 680px or 960px experiments.
The higher resolution model although selected to improve small-defect detection, lower performance was observed for this specific error class.
Packaging error detection remained weak (mAP50) = 0.208.
This result suggests increasing resolution is insufficient to improve small error detection

## 5. Overall Model Comparison

The following table compares the validation performance of the four experimental configurations.

| Model | Resolution | Precision | Recall | mAP50 | mAP50–95 | Inference (ms/image) |
|---|---:|---:|---:|---:|---:|---:|
| YOLOv8n | 640px | 0.650 | 0.617 | 0.623 | 0.348 | 4.4 |
| YOLOv8s | 640px | **0.781** | 0.619 | **0.681** | **0.424** | 7.9 |
| YOLOv8s | 960px | 0.700 | **0.681** | 0.650 | 0.329 | 19.6 |
| YOLOv8s | 1280px | 0.568 | 0.557 | 0.546 | 0.294 | 44.8 |

### 5.1 Key Findings

- **Best overall performance:** YOLOv8s at 640px achieved the highest mAP50 and mAP50–95.
- **Highest recall:** YOLOv8s at 960px achieved the highest recall (0.681).
- **Lowest inference time:** YOLOv8n at 640px was the fastest model (4.4 ms/image).
- **Effect of resolution:** Increasing resolution did not consistently improve detection performance.
- **Model selection:** YOLOv8s at 640px is currently the strongest candidate based on aggregate detection accuracy.

### 5.2 Engineering Interpretation

The results demonstrate a trade-off between detection performance and computational requirements.

Although the 960px model achieved higher recall, its inference time was substantially greater and its overall mAP was lower than the 640px YOLOv8s model.

The 1280px experiment also failed to improve aggregate detection performance.

Consequently, YOLOv8s at 640px is provisionally selected for final evaluation on the held-out test dataset.

*Note: All results are from the validation dataset. The final test-set evaluation has not yet been performed.*


## 6. Final Test-Set Evaluation

The YOLOv8s model at 640px was selected for final evaluation based on its validation performance.

The model was evaluated using the previously untouched test split containing 80 images and 79 annotated defect instances.

### Overall Results

| Metric | Test result |
|---|---:|
| Precision | 0.851 |
| Recall | 0.437 |
| mAP50 | 0.570 |
| mAP50–95 | 0.246 |
| Inference time | 8.3 ms/image |

### Per-Class Results

| Defect | Precision | Recall | mAP50 | mAP50–95 |
|---|---:|---:|---:|---:|
| Loose-meat | 0.774 | 0.333 | 0.720 | 0.244 |
| Packaging-error | 0.773 | 0.565 | 0.572 | 0.132 |
| Twisted-meat | 1.000 | 0.000 | 0.122 | 0.0367 |
| Unsealed | 0.856 | 0.851 | 0.865 | 0.573 |

The wrinkle category could not be evaluated because no annotated examples were present in the test dataset.

### Discussion

The final evaluation demonstrates that the selected model achieves relatively high precision but considerably lower recall.

Packaging-error detection achieved an mAP50 of 0.572, indicating reasonable detection capability, although localisation accuracy remains limited.

Twisted-meat detection performed poorly, with zero recall at the reported operating point. This result should be interpreted cautiously because only four instances were present in the test dataset.

Overall, the results demonstrate that the model can identify several categories of packaging defects, but its inconsistent recall and per-class performance limit its suitability for an automated inspection system without further improvement.

The test results also highlight the importance of evaluating individual defect categories rather than relying exclusively on aggregate performance metrics.

