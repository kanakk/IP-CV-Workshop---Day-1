# -*- coding: utf-8 -*-
"""
Author - Kanak Kawadiwale on Thu Nov  5 20:03:43 2020

@author: ag
"""
import cv2 
import numpy as np


print("Numpy Version - ",np.__version__)
print("opencv version - ",cv2.__version__)

im = cv2.imread('images/read_write.jpg')

print(type(im))
print(im.shape)
print(im.dtype)

cv2.imwrite('images_processed/image.jpg', im)

print("Image Saved")



