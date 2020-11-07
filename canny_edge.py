# -*- coding: utf-8 -*-
"""
Author - Kanak Kawadiwale on Thu Nov  5 20:03:43 2020

@author: ag
"""
import cv2
import numpy as np

#read any image for the edge detection
image = cv2.imread("images/edge.jpg")

#Converting the RGB image to HSV image to understand the image channels and 
#distribution of colors
hsv_converted = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Lower value for detecting red    
minmask_red = np.array([30,150,50])

# upper value for detecting red
maxmask_red = np.array([255,255,180])
    
#Now to seperate image luminance from color information we apply the inRange 
#function on HSV converted image with masking
mask = cv2.inRange(hsv_converted, minmask_red, maxmask_red)


cv2.imshow('HSV Image Converted',hsv_converted)
cv2.imshow('Original',image)

#finally applying the canny edge function on the image to detect the edges in image 
#we also need to decide the Upper and Lower bound values to help detect the edges sharply.
edges = cv2.Canny(image,100,200)


cv2.imshow('Edges',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
