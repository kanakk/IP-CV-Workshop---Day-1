# -*- coding: utf-8 -*-
"""
Author - Kanak Kawadiwale on Thu Nov  5 20:03:43 2020
@author: ag
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#img = cv.imread('images/haze2.jpg',0)
#equilized_img = cv.equalizeHist(img)
#res_img = np.hstack((img,equilized_img)) #stacking images side-by-side

#cv.imshow('res.png',res_img) 
#cv.waitKey(0)  
#cv.destroyAllWindows()  

img_read = cv.imread('images/haze2.jpg',0)

#Converting ndarray to 1D array 
histogram_array,total_bins = np.histogram(img_read.flatten(),256,[0,256])

#Calculating the cummulative_sum
cummulative_sum = histogram_array.cumsum()

#selecting the max values out of the flatten array
normalized_cdf = cummulative_sum * float(histogram_array.max()) / cummulative_sum.max()

plt.plot(normalized_cdf, color = 'b')
plt.hist(img_read.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

#Cumulative sum with masking array
cdf_masked = np.ma.masked_equal(cummulative_sum,0)

cdf_masked = (cdf_masked- cdf_masked.min())*255/(cdf_masked.max()- cdf_masked.min())

#filling the values in the array according to cumulative_sum
cdf_filled = np.ma.filled(cdf_masked,0).astype('uint8')

#applying the image transform 
img2 = cdf_filled[img_read]


cv.imshow("Original image",img_read)
cv.imshow("equlized image",img2)

cv.waitKey(0)

cv.destroyAllWindows()