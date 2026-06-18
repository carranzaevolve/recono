import os
import mysql.connector
import requests
import db_con
from PIL import Image

categories = {
    "bottle": "0",
    "can": "1",
    "box": "2",
    "container": "3",
    "tube": "4",
}

cur, conn = db_con.conn()

sql = "SELECT DISTINCT img_name FROM recono_boundig_boxes ORDER BY id DESC LIMIT 300"

cur.execute(sql)
bottles = cur.fetchall()

def yolobbox2bbox(cord_bottom, cord_left, cord_right, cord_top, width_img, height_img):	
    x_centro = (cord_left + ((cord_right - cord_left) / 2)) / width_img
    y_centro = (cord_top + ((cord_bottom - cord_top) / 2)) / height_img
    width = (cord_right - cord_left) / width_img
    height = (cord_bottom - cord_top) / height_img
	
    return x_centro, y_centro, width, height

x = 0
for btl in bottles:
    img_name = btl[0]
    print(img_name)

    img_url = "https://emetrix.com.mx/tracker/recono_images/" + img_name
    img_data = requests.get(img_url).content

    image_new_path = "Data/images/train/" + str(x) + ".jpeg"
    # Download image
    with open(image_new_path, "wb") as handler:
        handler.write(img_data)
    
    # Generate txt file for train
    with open("Data/labels/train/" + str(x) + ".txt", "w") as tx:        
    
        sql2 = "SELECT category, cord_bottom, cord_left, cord_right, cord_top, img_name FROM recono_boundig_boxes WHERE img_name = '" + img_name + "'"
        cur.execute(sql2)
        coord = cur.fetchall()

        # Get image size
        im = Image.open(image_new_path)
        w, h = im.size
        # print('width: ', w)
        # print('height:', h)

        for cor in coord:            
            x_centro, y_centro, width, height = yolobbox2bbox(float(cor[1]), float(cor[2]), float(cor[3]), float(cor[4]), w, h)
            tx.write(categories[cor[0]] + " " + str(x_centro) + " " + str(y_centro) + " " + str(width) + " " + str(height)  + "\n")
    
    x = x + 1

