#
# Dataset Generator
#
import os
import cv2
import multiprocessing
import qrcode
import random
import string
import numpy as np


#-- Defines --
FOLDER = 'dataset_qr'
IMAGE_SIZE = 21
STRING_LENGTH = 10
CHARACTER_SET = string.ascii_lowercase + string.ascii_uppercase + string.digits

#--
def RandomString():
    """
    Return a random string where characters are drawn 
    from a fixed set of characters.
    """
    return "".join(random.choice(CHARACTER_SET) for _ in range(STRING_LENGTH))




if not os.path.isdir(FOLDER):
    os.mkdir(FOLDER)


for data in np.random.choice(np.arange(1000, 10000), size=2500, replace=False):
    for version in [1, 2, 3, 4]:
        
        qr = qrcode.QRCode(
            version=version,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color='black', back_color='white')
        img = np.float32(np.asarray(img)) * 255
        img = np.dstack((img, img, img))

        cv2.imwrite(os.path.join(FOLDER, f"{data}-v{version}.png"), img)
