import numpy as np
import cv2 as cv

array1 = np.array([1, 2, 3])    #defined 1 X 3 array with numpy library
array2 = np.array([[1, 2], [3, 4]]) #defined 2 X 2 array 
array3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]] ])

print(array1[-1])
print(array2[0][1])
print(array3[0][1][1])

array4 = np.array([[1, 2, 3, 4, 5], 
                   [6, 7, 8, 9, 10], 
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20]]) # 4X5 matrix 

print(array4[1:3]) #numpy array -> *[start:end:step]


#matrix class not recommended in numpy library
#better use ndarray class

#setting ROI
array5 = np.zeros((1280, 1920, 3), np.uint8)
x, y, w, h = 100, 100, 300, 300
roi = array5[x:x+w, y:y+h]
print(array5.shape) #몇by몇 행렬인지 print하기
print(roi.shape) #몇by몇 행렬인지 print


#image input using python-openCV library
src = cv.imread("github.png", cv.IMREAD_GRAYSCALE)
print(src.ndim, src.shape, src.dtype) #print out github.png image details

#image output using python-openCV library 
cv.namedWindow("src", flags=cv.WINDOW_FREERATIO)
cv.resizeWindow("src", 400, 400)
cv.imshow("src", src)
cv.waitKey(0)
cv.destroyWindow("src")

