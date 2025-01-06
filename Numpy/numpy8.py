import numpy as np

np1 = np.array([1,2,3,4,5,6,7,8,9,10,3])

x = np.where(np1 == 3)
# returns the index 
print(x[0])


y = np.where(np1 %2 == 0)
print(y[0])

# to filter 
# x = [True,True,False,False,False,False,False,False,False]

filtered = []
# for thing in np1:
#     if thing%2 == 0:
#         filtered.append(True)
#     else:
#         filtered.append(False) 
           

# print(np1)
# print(filtered)
# print(np1[filtered])

# shortcut using num
filtered = np1 % 2 == 1
print(filtered)
print(np1[filtered])