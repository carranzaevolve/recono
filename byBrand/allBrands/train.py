from ultralytics import YOLO
import os

cwd = os.getcwd()

model = YOLO('yolov8n-cls.pt')  # load a pretrained model (recommended for training)
# model = YOLO("yolo11n-cls.pt")  # load a pretrained model (recommended for training)

data_path = cwd + "\Data"
# Train the model
results = model.train(data=data_path,
                      cfg="config.yaml",
                      epochs=30)
