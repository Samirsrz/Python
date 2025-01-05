import numpy as np

# slicing numpy arrays
np1  = np.array([1,2,3,4,5,6,7,8,9])
# output 2,3,4,5
print (np1[1:5])

# 4,5,6,7,8,9
print (np1[3:])

# 1,3,5
print(np1[0:5 :2]) 

# first to end step 2 kore agabe
# [1,3,5,7,9]
print(np1[::2])

# slicing 2D arrays
np2  = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# pull out a single item
# it will return 8
print(np2[1,2]) 

# 2,3  cause [0:1] dibe amader [1,2,3,4,5] and [1:3] eta amader dibe [2,3]
print(np2[0:1 ,1:3])

# [[ 8  9 10]]
print(np2[1: ,2:])

# slicing from both rows 2,3 and 7,8
print(np2[0:2 ,1:3])



