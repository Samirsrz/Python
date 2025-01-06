import numpy as np 
np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

# np2 =  np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
# print(np2.shape)

# important reshaping 1D array into 3rows and 4columns

np3= np1.reshape(3,4)
print(np3)
print(np3.shape)

# reshape into 3D
np4 = np1.reshape(2,3 ,2)
print(np4)
print(np4.shape)

#back to 1D 
np5 = np1.reshape(-1)
print(np5)