"""
A script designed to 1) resize all of the downloaded images to desired dimension (DEFAULT 64x64 pixels) and 2) rename images in folders from 1.png to n.png for ease of use in training
"""

import os
import scipy.misc
import random
import shutil
import numpy as np
import PIL
root = './images_512images'

# Set your own PATH
# PATH = os.path.normpath('C:/Users/danie/GANGogh/images_512/')

for subdir, dirs, files in os.walk(root):
    style = subdir[2:]
    # if 'landscape' not in style:
    #     continue
    name = style
    if len(style) < 1:
        continue
    # try:
    #     os.stat(PATH + name)
    # except:
    #     os.mkdir(PATH + name)

    i = 0
    for f in files:
        source = style + '\\' + f
        # print(str(i) + source)
        try:
            image = scipy.misc.imread(source)
            # image = scipy.misc.imresize(image, (512, 512))

            if len(image.shape) == 3 and image.shape[-1] > 3:
                print("RGBY:", image.shape)
                # shutil.move(source, os.path.normpath('C:/Users/danie/PycharmProjects/DCGAN-tensorflow/bad_data/' + f))
                # image = image[...,:3]
                image = PIL.Image.open(source)
                image = image.convert("RGB")
                image = np.asarray(image, dtype=np.float32) / 255
                image = image[:, :, :3]
                print(source)
                scipy.misc.imsave(source, image)
                
                # scipy.misc.imsave(source, image)
                # raise Exception("go check")

            elif len(image.shape) == 2:
                stacked = np.stack((image,)*3, axis=-1)
                scipy.misc.imsave(source, stacked)
                print("grayscale", image.shape)
                print(source)

                

                # raise Exception("go check")

            else:
                i += 1
        except Exception as e:
            print('missed it: ' + source, e)
