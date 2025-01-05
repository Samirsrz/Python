import numpy as np 
np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

# np2 =  np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
# print(np2.shape)

# important reshaping 1D array into 3rows and 4columns

np3= np1.reshape(3,4)
print(np3)
print(np3.shape)