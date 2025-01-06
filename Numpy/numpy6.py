import numpy as np
# 2D array
np2 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])

# for x in np2:
#     for y in x:
#         print(y)


array_3d = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],  
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]] 
])

# for x in array_3d:
#     for y in x:
#         for z in y:
#             print(z)


# easier way to print
# use  np.nditer(your_array)
for x in np.nditer(array_3d):
    print(x)

