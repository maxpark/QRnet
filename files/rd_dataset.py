import qrcode
import qrcodes
from qrcodes import IMAGE_SIZE

import matplotlib.pyplot as plt

from keras import layers
from keras import models
from keras.preprocessing import image
from keras.utils import to_categorical


NUM_OUTPUTS = len(qrcodes.CHARACTER_SET)
#--
NUM_TRAIN_IMAGES = 500
NUM_VALID_IMAGES = 50
NUM_TEST_IMAGES = 5
#
HSIZE_IMAGE = 21
VSIZE_IMAGE = 21

#
#img = qrcode.make("asdfgjkl1234")
#img.save('./tmp.png')
#s


# Validation set

#print("Creating {} random test images ... ".format(NUM_TEST_IMAGES), end="", flush=True)
train_images, train_labels = qrcodes.getRandomBatch(size=NUM_TRAIN_IMAGES)
#print("done")

train_images = train_images.reshape(NUM_TRAIN_IMAGES, HSIZE_IMAGE, VSIZE_IMAGE)

print(train_images.shape)

#- Display Train Image sample
for i in range(3*4):
    plt.subplot(3, 4, i+1)
    plt.imshow(train_images[i], 'gray')

plt.suptitle("train images", fontsize=12)
plt.show()

#print(string(train_labels[0]))

