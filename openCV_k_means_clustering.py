import cv2 as cv
import numpy as np

'''
retval, bestLabels, centers = cv.kmeans(
    data,
    K,
    bestlabels = None,
    criteria,
    attempts,
    flags
)
'''

src = cv.imread("tomato.jpg") 

data = src.reshape(-1,3).astype(np.float32)

K = 3

criteria = (cv.TERM_CRITERIA_MAX_ITER + cv.TERM_CRITERIA_EPS, 10, 0.001)
retvals, bestLabels, centers = cv.kmeans(data, K, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

centers = centers.astype(np.uint8)
dst = centers[bestLabels].reshape(src.shape)

cv.imshow("dst", dst)
cv.waitKey()
cv.destroyAllWindows()
