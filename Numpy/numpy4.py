import numpy as np

np1 = np.array([0,1,2,3,4,6])

# create a view
np2 = np1.view()
print(np1)
print(np2)

np1[0]= 22 
# np1 will be updated as np2[0]=44
np2[0]=44
# np2 will also be updated
print(np1)
print(np2)


np2 = np1.copy()
np1[1]= 55 
# np22 will not be be updated
np2[1] = 66
print(np1)
print(np2)



# in view amra jodi np1 or np2 jetai change kori oitai change hoye jabe but copy function e jeta change korba shudhu oitai change hobe
