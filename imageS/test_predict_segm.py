from ultralytics import YOLO
from PIL import Image
from matplotlib import pyplot as plt
import cv2
import numpy as np
from pathlib import Path
import request_example

model_path = 'runs/segment/train4/weights/last.pt'  

image_path = 'test_img/643678501.jpeg'

img = cv2.imread(image_path)
H, W, _ = img.shape

model = YOLO(model_path)

results = model.predict(image_path)

#  Iterate detection results (helpful for multiple images)
for r in results:
    img = np.copy(r.orig_img)
    img_name = Path(r.path).stem # source image base-name

    # Iterate each object contour (multiple detections)
    for ci,c in enumerate(r):
        #  Get detection class name
        label = c.names[c.boxes.cls.tolist().pop()]

        # Create binary mask
        b_mask = np.zeros(img.shape[:2], np.uint8)

        #  Extract contour result
        contour = c.masks.xy.pop()
        #  Changing the type
        contour = contour.astype(np.int32)
        #  Reshaping
        contour = contour.reshape(-1, 1, 2)


        # Draw contour onto mask
        _ = cv2.drawContours(b_mask,
                            [contour],
                            -1,
                            (255, 255, 255),
                            cv2.FILLED)
        
        # Isolate object with transparent background (when saved as PNG)
        isolated = np.dstack([img, b_mask])

        #  Bounding box coordinates
        x1, y1, x2, y2 = c.boxes.xyxy.cpu().numpy().squeeze().astype(np.int32)
        # Crop image to object region
        iso_crop = isolated[y1:y2, x1:x2]

        new_file_path = 'img_result/' + str(img_name) + '_' + label + '-' +  str(ci) + '.png'

        # Save isolated object to file
        _ = cv2.imwrite(new_file_path, iso_crop)

        res = request_example.request_analyze(new_file_path)

        print(res)

