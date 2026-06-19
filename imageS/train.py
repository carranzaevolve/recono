from ultralytics import YOLO

model = YOLO('yolov8n-seg.pt') 

#results = model.train(data=r'C:\Users\aca18\Documents\evolve\imageSegmentation\Data', epochs=20, imgsz=64)

model.train(data='config.yaml', epochs=20, imgsz=640)