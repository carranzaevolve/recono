import os
import mysql.connector
import requests
import db_con
from PIL import Image

categories = {
    "bottle": "0"
}

cur, conn = db_con.conn()

sql = "SELECT DISTINCT img_name FROM recono_boundig_boxes WHERE idFoto in ( \
        33875595,33949624,33949594,33948804,33948202,33947068,33949862,33946872,33945920,33945586, \
        33944803,33942386,33942060,33941186,33940897,33940593,33937186,33936743,33935051,33934269, \
        33934257,33934069,33933998,33933164,33932629,33929306,33929302,33929299,33926846,33926110, \
        33925717,33925478,33925007,33924916,33946907,33944582,33944511,33944495,33942616,33944824, \
        33943160,33943135,33941910,33942443,33943088,33942862,33942869,33941188,33941162,33941446, \
        33941164,33941321,33941280,33941349,33941495,33941546,33941556,33941567,33941578,33941582, \
        33941752,33940297,33942047,33940636,33942134,33942060,33940871,33941021,33940897,33941119, \
        33941105,33941136,33941152,33941154,33941163,33941212,33938751,33938787,33938857,33938813, \
        33939053,33939057,33939078,33939374,33939395,33939423,33939526,33939563,33939735,33939792, \
        33938337,33940200,34004150,34004159,34006093,34006104,34005364,34005313,34005377,34005371, \
        34005401,33973089,33973439,33973116,33973128,33973292,33973193,33973230,33973439,33973513, \
        33973758,33974105,33974129,34005574,34005589,34005881,34006069,34006304,34006122, \
        34771300,34160276,34602102,34558889,31779772,34616822,34161916,34558838,34357702,34960309,\
        34039154,32819065,34123597,33836391,33349372,31729982,34357688,34512832,33265201,34351407,\
        33740463,33808431,34285164,33730925,34699173,33978977,34518782)"

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
    # image_new_path = "Data/images/validation/" + str(x) + ".jpeg"
    # Download image
    with open(image_new_path, "wb") as handler:
        handler.write(img_data)
    
    # Generate txt file for train
    with open("Data/labels/train/" + str(x) + ".txt", "w") as tx:        
    
        sql2 = "SELECT category, cord_bottom, cord_left, cord_right, cord_top, img_name FROM recono_boundig_boxes \
            WHERE is_valid = 1 and category = 'bottle' AND img_name = '" + img_name + "'"
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

