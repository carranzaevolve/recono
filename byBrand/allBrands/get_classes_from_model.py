from ultralytics import YOLO

model = YOLO('runs/classify/train32/weights/last.pt')

for id in model.names: 
    print(model.names[id])