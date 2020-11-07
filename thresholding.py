# -*- coding: utf-8 -*-
"""
Author - Kanak Kawadiwale on Thu Nov  5 20:03:43 2020

@author: ag
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('images/thresholding.jpg',0)

# Binary thresholding technique 
ret1,thresh1 = cv2.threshold(img,129,255,cv2.THRESH_BINARY)

# Otsu's thresholding on the same image 
thresh2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

# Gaussian Filtered image with Otsu's thresholding for better results
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,thresh3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(222),plt.imshow(thresh1),plt.title('Simple Binary thresholding')
plt.xticks([]), plt.yticks([])

plt.subplot(223),plt.imshow(thresh2),plt.title('Adaptive Thresholding')
plt.xticks([]), plt.yticks([])

plt.subplot(224),plt.imshow(thresh3),plt.title('Otsu Thresholding with Filter')
plt.xticks([]), plt.yticks([])

plt.show()
