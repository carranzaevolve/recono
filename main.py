
from matplotlib import pyplot as plt
import keras_ocr


pipeline = keras_ocr.pipeline.Pipeline()

images = [keras_ocr.tools.read(img) for img in [
        # 'https://storage.googleapis.com/gcptutorials.com/examples/keras-ocr-img-1.jpg',
        'images/2065101232.jpeg'
          ]
        ]

# print(np.shape(images))

# images = keras_ocr.tools.read('https://upload.wikimedia.org/wikipedia/commons/b/bd/Army_Reserves_Recruitment_Banner_MOD_45156284.jpg')


prediction_groups = pipeline.recognize(images)[0]
# print(prediction_groups[1][0])

words_reco = []
for arr in prediction_groups:
    for tx in arr:
        if isinstance(tx, str):
          words_reco.append(tx)


print(words_reco)

# if 'pasos' in words_reco:
#    print('Es Los pasos')






# print(type(prediction_groups))

# prediction_image_1 = prediction_groups[0]
# for text, box in prediction_image_1:
#     print(text)



# predicted_image = prediction_groups[0]
# for text, box in prediction_groups:
#     print(text)
    # print(box)
    # print('+++++++++++++++')
# for text, box in predicted_image:
#     print(text)

# fig, axs = plt.subplots(nrows=len(images), figsize=(20, 20))
# for ax, image, predictions in zip(axs, images, prediction_groups):
#     keras_ocr.tools.drawAnnotations(image=image, predictions=predictions, ax=ax)
#
# plt.show()