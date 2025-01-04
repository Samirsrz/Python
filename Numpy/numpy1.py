import numpy as np
list1 = [1,2,3,4,5]

list2 = [[4,5,6,7],[8,9,10,11]]

np1 = np.array([0,2,3,5,4,8,9,1])
print(np1.shape)


np2 =  np.arange(10) 
#  0 - 9 output dibe
print(np2)


np3 = np.arange(0,10, 3)
# 0,3,6,9
print(np3)

np4 = np.zeros(10)
print(np4)

# multi dimentional zeros
np5 = np.zeros((2,10))
# [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
print(np5)

# Full function
np6 = np.full((10), 6)
# 6 6 6 6 6 6 6 6 6 6
print(np6)

# multi Dimensional Full
np7 = np.full((2,10), 7)
print(np7)

# converting pythons lists to np
my_list = [1,2,3,4,5,6,7,8]
np9 = np.array(my_list)
print(np9)
