from ultralytics import YOLO
# from Data import load_dataset
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np


# dataset = load_dataset("kili-technology/plastic_in_river")
# img = dataset["test"][0]["image"]
img = 'test_img/2025021267acda56345c9.jpeg'
model = YOLO("runs/detect/train3/weights/last.pt")

results = model(img)
 
# Loop through detections
for result in results:
    for box in result.boxes:
        x1, y1, x2, y2 = box.xyxy[0].int().tolist()  # Bounding box coordinates
        print(f"Coordinates: {x1}, {y1}, {x2}, {y2}")

result.show()  # Display the image with bounding boxes
result.save("output.png")
# res = res.plot(line_width=1)
# res = res[:, :, ::-1]
# res = Image.fromarray(res)
# res.save("output.png")
