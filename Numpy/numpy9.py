import numpy as np

arr1 = np.array([[1,2,4,3],[5,6,7,8]])
arr2 = np.array([[11,22,44,33],[55,66,77,88]])

arr = np.concatenate((arr1,arr2), axis=1)
print(arr)

