from ultralytics import YOLO
from PIL import Image

import os
import glob
import time


timestr = time.strftime("%Y%m%d-%H%M%S")

# train8 was the lastone withon competition classes
# load custom model
model = YOLO('runs/classify/train29/weights/last.pt')

path_dir = 'test_images'
# predict on an image

images = glob.glob(path_dir + '/*')

with open("output_text/"+timestr+".txt", "w") as tx:
    # print(images)
    for f in images:
        img_name = os.path.basename(f)
        print(img_name)
        tx.write(img_name+"\n")
        img_path =path_dir + "/" + img_name

        '''
        results = model.predict(img_path)
        names_dict = results[0].names
    
        probs = results[0].probs
    
    
        for r in results:
            for c in range(0, 5):
                id =r.probs.top5[c]
                print(id, r.names[id], r.probs.top5conf.numpy()[c])
        '''
        #print('CROP IMAGE')

        im = Image.open(img_path)

        width, height = im.size

        bootom_to_crop = height * .08
        # Setting the points for cropped image
        left = 1
        top = height * .25
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
                dfr = str(id) + " - " + r.names[id]+ " - " + str(r.probs.top5conf.numpy()[c])
                tx.write(dfr + "\n")
            print('----------------\n\n')
        #im1.show()