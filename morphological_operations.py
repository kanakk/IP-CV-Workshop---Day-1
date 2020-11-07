# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 10:41:36 2020
@author: ag
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/morph3.png')

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5,5),np.uint8)

#In erossion technique pixel in the original image will be considered 1 only if 
#all the pixels under the kernel is 1, otherwise it is made to 0 as erossion.
erosion = cv2.erode(gray_image,kernel,iterations = 1)

# In dilation technique pixel element is 1 if atleast one pixel value under the kernel is 1
dilation = cv2.dilate(gray_image,kernel,iterations = 1)

#Opening operation is equal to Erossion followed by Dilation - a combined version 
opening = cv2.morphologyEx(gray_image, cv2.MORPH_OPEN, kernel)

#Closing operation is equal to Dilation followed by Erossion - a combined version 
closing = cv2.morphologyEx(gray_image, cv2.MORPH_CLOSE, kernel)

#Displaying the processed images using imshow function
cv2.imshow("Original Image ",img)
cv2.imshow("Erossion",erosion)
cv2.imshow("Dilation",dilation)
cv2.imshow("Opening",opening)
cv2.imshow("Closing",closing)

#Wait untill closed by user
cv2.waitKey(0)

#Destroy the invoked display windows 
cv2.destroyAllWindows()