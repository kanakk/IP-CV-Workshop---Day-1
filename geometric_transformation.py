# -*- coding: utf-8 -*-
"""
Author - Kanak Kawadiwale on Thu Nov  5 20:03:43 2020

@author: ag
"""

import cv2
import numpy as np

#################### Scaling the Image ################

img = cv2.imread('images/haze.png')
cv2.imshow('Original Image ',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#scaling is based totally on the scaling factor that is being passed to the resize function
scaled_image = cv2.resize(img,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)

cv2.imshow('Scaled Image',scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

######################## Translation of Image ########

rows,cols = img.shape[:2]

#To translate the image, you need the image matrix that would change the 
#rows and coloumns of the image 
float_matrix = np.float32([[1,0,100],[0,1,50]])

#wrapAffine function helps in translating the image according float matrix 
translated_image = cv2.warpAffine(img,float_matrix,(cols,rows))

cv2.imshow('Translated Image',translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

######################### Rotating the Image ############
img = cv2.imread('images/haze.png')
rows,cols = img.shape[:2]

#To rotate the image, you need the image matrix that would change the 
#rows and coloumns of the image according to your need
rotation_matrix = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)

rotated_image = cv2.warpAffine(img,rotation_matrix,(cols,rows))

cv2.imshow('Image Rotation',rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()