# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 20:13:21 2017

@author: henriheinonen
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

image = mpimg.imread('test.jpg')
plt.figure(1)
plt.imshow(image)
plt.show()

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
plt.figure(2)
plt.imshow(gray, cmap='gray')
plt.show()

kernel_size = 3
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size), 0)

low_threshold = 1
high_threshold = 10
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

plt.figure(3)
plt.imshow(edges, cmap='Greys_r')
plt.show()