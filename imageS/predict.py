from ultralytics import YOLO
from PIL import Image
from matplotlib import pyplot as plt
import cv2
import numpy as np
from pathlib import Path


model_path = 'runs/segment/train4/weights/last.pt'  

image_path = 'test_img/1630197101.jpeg'

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

        # Save isolated object to file
        _ = cv2.imwrite(f'img_result/{img_name}_{label}-{ci}.png', iso_crop)

# Access the masks
#masks = results[0].masks
#mask = masks[0].data.squeeze().cpu().numpy() * 255  # For multi-class, iterate over masks
#mask = mask.astype(np.uint8) # Convert mask to uint8 if needed
#cv2.imwrite('segmented_mask.png', mask)# Save the mask

# Show mask wiht plot
#new_result_array = results[0].plot()
#plt.figure(figsize=(12, 12))
#plt.imshow(new_result_array)
#plt.show()

'''
result = results[0]
masks = result.masks

# How many segementation were found
len(masks)

mask1 = masks[0]

print(len(masks))

mask = mask1.data[0].numpy()
print(mask)
'''
#polygon = mask1.xy[0]

#mask_img = Image.fromarray(mask,"I")
#mask_img

'''
for result in results:
    for j, mask in enumerate(result.orig_img):

        mask = mask * 255

        mask = cv2.resize(mask, (W, H))

        cv2.imwrite('./output.png', mask)
'''