
import os
import requests

def request_analyze(img_path):
    file_name = os.path.basename(img_path)
    print(img_path)
    print(file_name)
    #url = "http://54.189.203.61/analyzeImage?idFoto=" + str(idFoto)
    url = "http://127.0.0.1:5000/cropImageSegmentation"

    payload = {'category': 'bottle'}
    files=[
    ('image',(file_name,open(img_path,'rb'),'image/jpeg'))
    ]
    headers = {
    'Api-Token': 'HfHOm4at0DiuUs7ti8XifqQjZ7o66J38vsBLESMIIxoMyKPswj3rKtB0sDs7Kk1v'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return response.text
    # print(response.text)

# request_analyze('img_result/1618735902_bottle-0.png')
