import cv2 as cv
import numpy as np
'''
python color space transformation 
dst = cv.cvtColor(
    src,
    code,
    dstCn = None
)
'''

tgt = cv.imread("O8.jpg")
dst = cv.cvtColor(tgt, cv.COLOR_BGR2HSV)

save1 = cv.imwrite("O8_BGR2HSV.jpeg", dst, (cv.IMWRITE_JPEG_QUALITY, 100, cv.IMWRITE_JPEG_PROGRESSIVE, 1))
cv.imshow("dst", dst)
cv.waitKey(0)
cv.destroyAllWindows()