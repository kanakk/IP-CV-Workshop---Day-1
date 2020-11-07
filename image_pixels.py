# -*- coding: utf-8 -*-
"""
Author - Kanak Kawadiwale on Thu Nov  5 20:03:43 2020

@author: ag
"""
#import libraries into your code
import numpy as np
import cv2 as cv

#Reading the image from your local machine
img = cv.imread('images/read_write.jpg')
cv.imshow("image display", img)
cv.waitKey(0)  
cv.destroyAllWindows()  

#Access the pixel values of image
px = img[100,100]
print("Pixel RGB value at certain Pixel location ",px)

#Extract the Color Space values specifically 
blue = img[100,100,0]
print(blue)


#Changing the color of certain pixel using numpy
img[100,100] = [255,255,255]
print("Changed color of Pixel at point 100x,100y", img[100,100])

#Changing the whole red color in image to white 
#Syntax -> img [i,j,k] where i,j is co-ordinate value and k is channel (B=0,G=1,R=2)
img[:,:,1] = 0

#Important functions in Numpy for Image Processing which can get you the properties of Images
print("ravel - ",img.ravel())
print("image shape - ", img.shape)
print("Total Pixels in Image - ", img.size)
print("Image Data Type - ", img.dtype)

cv.imshow("image display", img)
cv.waitKey(0)  
cv.destroyAllWindows()  