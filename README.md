# Automated Visual Inspection of Packaged Pork Rashers 
## 1. Project Overview
This project investigates the use of computer vision and machine learning for automated visual inspection of packaged pork rashers. 

The aim of this project is to develop an object detection system capable of identifying and localising visible product and packaging errors in RGB images. This system used the YOLO object detection framework to classify defects and predict their location using bounding boxes.

The intended engineering application is automated visual quality inspection in food packaging processes. This project is a computational investigation using an existing image dataset and does not constitute validation of an employed system.

## 2. Dataset and Methodology
This project uses Version 4 of the Pork Rasher Error(Packaging) Computer Vision Dataset obtained from Roboflow. The dataset contains 3,549 annotated images divided into training (3349), validation (120) and test (80) splits. Images are provided in an RGB format with YOLO Format annotated bounding boxes.

Five defect categories are present in the dataset
- Loose Meat
- Packaging-Error
- Twisted Meat
- Wrinkle
- Unsealed Meat

This Project used the YOLOv8 object detection framework. Experiments compare YOLOv8n and YOLOv8s model configurations at input resolutions of 640, 960 and 1280 pixels. Model performance is assessed using precision, recall mean average precision (mAP) and inference time.

Original dataset splits were retained for model development and evaluation.

## 3. Repository Structure
The repository is structured into separate directories for source code, testing code and relevant supporting documentation.

MMA3001-Pork-Inspection/

│

├── src/

│   ├── __init__.py

│   ├── data_loader.py

│   ├── model.py

│   ├── evaluation.py

│   └── train.py

│

├── tests/

│   ├── test_data_loader.py

│   ├── test_model.py

│   ├── test_evaluation.py

│   └── test_report.txt

│

│
├── requirements.txt

├── README.md

├── LICENSE

└── experimental_log.md

* src/: contains the python functions for dataset handling, model loading, training and evaluation
* tests/: contains automated tests and the test report
* requirements.txt: Lists the python dependencies.
* experimental_log.md: Records model experiments, comparisons and results.
* LICENSE: Defines license for project source code

## 4. Code Documentation
HTML documentation for the project's Python source modules is available in the docs directory.

## 5. Installation and Usage
### Requirements
The project uses python and the Ultralytics YOLOv8 framework. Required python packages are listed in requirements.txt.

### Installation
Clone the repository:

git clone https://github.com/dot-meh/MMA3001-Pork-Inspection.git

cd MMA3001-Pork-Inspection

Install the dependencies

pip install -r requirements.txt

### Dataset Setup

Download Version 4 of the Pork Rasher Error(Packaging) dataset from Roboflow universe.

Extract the dataset and ensure that its directory structure contains the train, valid and test folders, along with the dataset configuration YAML file.

The dataset is not included in the repository.

### Running the Code
The python modules provide functions for dataset handling, model loading, training and evaluation.

Model training can be initiated from the command line using:

python -m src.train --data path/to/data.yaml --weights yolov8n.pt --output results

Additional training parameters can be specified using --imgsz, --batch, --epochs and --device.

Automated tests can be run using:

python -m pytest -v

## 6. Results and Limitations
### Results
Four YOLO configurations were compared using the validation dataset. YOLOv8s at 640 pixel input resolution achieved the best overall performance.

| Model | Input resolution (px) | mAP50 | mAP50–95 | Inference time (ms/image) |
|:---|---:|---:|---:|---:|
| YOLOv8n | 640 | 0.623 | 0.348 | 4.4 |
| YOLOv8s | 640 | **0.681** | **0.424** | 7.9 |
| YOLOv8s | 960 | 0.650 | 0.329 | 19.6 |
| YOLOv8s | 1280 | 0.546 | 0.294 | 44.8 |

The selected YOLOv8s 640 model was subsequently evaluated on the held-out test set, achieving an mAP50 of 0.570 and an mAP50–95 of 0.246.

### Limitations
The dataset exhibits substantial class imbalance, with packaging error and unsealed defects accounting for the majority of annotations. The wrinkle category is not represented in the validation or test sets, preventing evaluation of its detection performance.

The relatively small validation and test sets limit statistical confidence of the reported performance measurements. Additionally, related source images may occur across different dataset splits, potentially reducing their independence. 

The project investigates image based detection, not an implemented industrial inspection system. Consequently, the results do not establish performance under real production line conditions.

## 7. References and Attribution
### Dataset
Pork Rasher Error(Packaging), Version 4, Roboflow Universe.

https://universe.roboflow.com/hello-2aqe0/pork-rasher-error-packaging/dataset/4

### Software
* Ultralytics YOLOv8: https://github.com/ultralytics/ultralytics
* Python: https://www.python.org/

This project uses source code distributed under the MIT License, see License for details.


