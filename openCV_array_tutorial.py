import numpy as np

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


