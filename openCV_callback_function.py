import cv2 as cv
import numpy as np

def mouse_event(event, x, y, flags, param):
    global radius
    if event == cv.EVENT_FLAG_LBUTTON:
        cv.circle(param, (x, y), radius, (0, 255, 0), 2)
        cv.imshow("draw", src)
        
    elif event == cv.EVENT_FLAG_RBUTTON:
        if flags > 0:
            radius += 1
        elif radius > 1:
            radius -= 1

radius = 3
src = np.full((500, 490, 3), 255, dtype=np.uint8)

cv.imshow("draw", src)
cv.setMouseCallback("draw", mouse_event, src)
cv.waitKey()
cv.destroyAllWindows()

     