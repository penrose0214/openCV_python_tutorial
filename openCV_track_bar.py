import cv2 as cv
import numpy as np

def onChangeBlue(pos):
    global b
    b = pos
    cv.imshow("any name", createImage(b, g, r))
    
    def createImage(b, g, r):
        return np.full((500, 500, 3), (b, g, r), dtype=np.uint8)
    
    b, g, r = 0, 0, 0
    cv.namedWindow("any name")
    cv.