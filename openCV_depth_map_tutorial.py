import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

L_img = cv.imread('Left_image.png', 0)
R_img = cv.imread('Right_image.png', 0)

stereo = cv.StereoBM_create(numDisparities = 16, blockSize = 15)
disparity = stereo.compute(L_img, R_img)

plt.imshow(disparity, cmap='gray') #cmap = 'gray' refers to gray-scale image
plt.show()

print(disparity)
