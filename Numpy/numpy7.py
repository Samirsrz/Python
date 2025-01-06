import numpy as np

# np.sort()
np1 = np.array([6,7,8,9,0,1,2,5,3])
print(np.sort(np1))

np2 = np.array(["john","arra","tina","samir","zim"])
print(np.sort(np2))

# booleans
np3 = np.array([True,False,False,True])
print(np.sort(np3))


# return a copy not change the original
np4 = np.array([[6,7,1,3],[2,5,8,0]])

print(np.sort(np4))