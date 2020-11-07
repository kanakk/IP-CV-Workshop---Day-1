# -*- coding: utf-8 -*-
"""
Author - Kanak Kawadiwale on Thu Nov  5 20:03:43 2020

@author: ag
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('images/noisy.png')

#Gaussian Filters are generally used for blurring the image and removing the noise
gasussian_filter = cv.GaussianBlur(img,(15,15),0)

#Median filter is primarily used when there are salt and pepper noise in the image.
median_filter = cv.medianBlur(img,5)

#Bilateral filter preserves the sharp edges while removing the noise from images.
bilateral_filter = cv.bilateralFilter(img,9,15,15)

plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(222),plt.imshow(gasussian_filter),plt.title('Gaussian Filter')
plt.xticks([]), plt.yticks([])

plt.subplot(223),plt.imshow(median_filter),plt.title('Median Filter')
plt.xticks([]), plt.yticks([])

plt.subplot(224),plt.imshow(bilateral_filter),plt.title('Bilateral Filter')
plt.xticks([]), plt.yticks([])

plt.show()