import cv2 as cv
import numpy as np

def mouse_event(event, x, y, flags, param):
    global radius
    if event == cv.circle(param, (x, y), radius, (255, 0, 0), 2):
        cv.imshow("draw", src)
        
    elif event == cv. EVENt_MOUSEWHEEL:
        if flags > 0:
            radius += 1
        elif radius > 1:
            radius -= 1

radius = 3
src = np.full((500, 500, 3), 255, dtype=np.uint8)
     