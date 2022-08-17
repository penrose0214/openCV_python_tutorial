import cv2 as cv

src = cv.imread("tomato.jpg")
hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)

h, s, v = cv.split(hsv)

orange = cv.inRange(hsv, (8, 100, 100), (20, 255, 255))
blue = cv.inRange(hsv, (110, 100, 100), (130, 255, 255))
mix_color = cv.addWeighted(orange, 1.0, blue, 1.0, 0.0)

dst = cv.bitwise_and(hsv, hsv, mask = mix_color)
dst = cv.cvtColor(dst, cv.COLOR_HSV2BGR)

cv.imshow("dst", dst)
cv.waitKey(0)
cv.destroyAllWindows()


