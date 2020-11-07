# -*- coding: utf-8 -*-
"""
Author - Kanak Kawadiwale on Thu Nov  5 20:03:43 2020

@author: ag
"""
import cv2 
import numpy as np 
  
# read any image or shape
image = cv2.imread('images/contour.jpg') 
  
# Pre-processing the image and converting it to Grayscale image 
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
  
# Find Canny edges on the image to detect the contours
can_edge= cv2.Canny(image_gray , 30, 200) 
  
#apply the findContour function on edge detected image to find the contours properly.
contours_detected, contour_hierarchy = cv2.findContours(can_edge,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
  
cv2.imshow('Edges after contour detection', can_edge) 
cv2.waitKey(0) 
  
  # -1 in the parameter denotes drawing all contours detected over the image
cv2.drawContours(image, contours_detected, -1, (0, 255, 0), 3) 

print("Total Contours found -> " + str(len(contours_detected))) 
  
cv2.imshow('Contours Found In Image', image) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 