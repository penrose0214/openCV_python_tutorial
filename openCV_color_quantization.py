import numpy as np
import cv2 as cv

'''
This code is for color-quantization of certain input image file;
color quantization is necessary for saving space in given memory

pros:
noise-resistant

cons:
instance-based learning -> slow process
-> requires reduction in demensionality in order to speed up
'''
src = cv.imread("tomato.jpg")
src_reshaped = src.reshape((-1, 3)) # -1 in reshape(-1, 3) means that original src matrix form will be fit into n X 3 matrix where number n will be formatted accordingly
src_reshaped = np.float32(src_reshaped)
#above 2 lines can be replaced with src.reshaped = src.reshape((-1, 3)).astype(np.float32)

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 0.000001)
K = 5 # smaller K-value --> simpler colors 
retval, bestL, center = cv.kmeans(src_reshaped, K, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

#formatting color-quantized matrix file back to visible image file
center = np.uint8(center)
final = center[bestL.flatten()]
final2 = final.reshape((src.shape))

cv.imshow('final2', final2)
cv.waitKey(0)
cv.destroyAllWindows

'''
참고 블로그 URL: http://www.gisdeveloper.co.kr/?p=7123
참고 도서: C#과 파이썬을 활용한 OpenCV4 프로그래밍 
'''