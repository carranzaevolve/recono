from ultralytics import YOLO

model = YOLO('runs/classify/train4/weights/last.pt')
model.export(format='tflite')