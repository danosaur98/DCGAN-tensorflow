"""
A script designed to 1) resize all of the downloaded images to desired dimension (DEFAULT 64x64 pixels) and 2) rename images in folders from 1.png to n.png for ease of use in training
"""

import os
import scipy.misc
import random
import shutil

root = './images_256images'

# Set your own PATH
# PATH = os.path.normpath('C:/Users/danie/GANGogh/images_512/')

for subdir, dirs, files in os.walk(root):
    style = subdir[2:]
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
            image = scipy.misc.imresize(image, (512, 512))
            if len(image.shape)!=3 or image.shape[-1] != 3:
                print("error!", str(i) + source)
                shutil.move(source, os.path.normpath('C:/Users/danie/PycharmProjects/DCGAN-tensorflow/bad_data/' + f))
                # scipy.misc.imsave(PATH + name + '\\' + str(i) + '.png', image)
            else:
                i += 1
        except Exception as e:
            print('missed it: ' + source, e)
