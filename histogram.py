# -*- coding: utf-8 -*-
"""
Author - Kanak Kawadiwale on Thu Nov  5 20:03:43 2020
@author: ag
"""
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

#Plotting histograms using matplotlib library
img = cv.imread('images/read_write.jpg')

#raw pixel data of the image in numercial form 
ravel_data = img.ravel()

plt.hist(ravel_data,256,[0,256]); plt.show()

#Considering the color standard of RGB.
colorspace = ('b','g','r')

for iterate,col in enumerate(colorspace):

    rgb_histogram = cv.calcHist([img],[iterate],None,[256],[0,256])

    plt.plot(rgb_histogram,color = col)

    plt.xlim([0,256])

plt.show()

cv.imshow("original image", img)
cv.waitKey(0)
cv.destroyAllWindows()
