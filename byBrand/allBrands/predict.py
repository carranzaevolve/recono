from ultralytics import YOLO
from PIL import Image

# load custom model
model = YOLO('runs/classify/train4/weights/last.pt')

#print(model.names) 

img_path = 'test_images/barfoot_pinotnoir.jpeg'
# predict on an image
results = model.predict(img_path)

names_dict = results[0].names

probs = results[0].probs


for r in results:
    for c in range(0, 5):
        id =r.probs.top5[c]
        print(id, r.names[id], r.probs.top5conf.numpy()[c])

print('CROP IMAGE')

im = Image.open(img_path)

width, height = im.size

bootom_to_crop = height * .10
# Setting the points for cropped image
left = 1
top = height * .30
right = width-1
bottom = height-bootom_to_crop

# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
# print(names_dict)
# print(probs)
results2 = model.predict(im1)

names_dict = results2[0].names

probs = results2[0].probs

for r in results2:
    for c in range(0, 5):
        id =r.probs.top5[c]
        print(id, r.names[id], r.probs.top5conf.numpy()[c])

im1.show()
