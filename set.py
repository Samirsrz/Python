# unordered unique elements ke print kore
k = set([2,3,2,2,3,3,1,1,1,2])
# print(k) 
# output {1,2,3}


a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9,10}
union = a.union(b)
# print(union)
intersection = a.intersection(b)
# print(intersection)

# /symmetric difference --> a^b All of the elements in either a or b but not both
symmetricdifference = a^b
print(symmetricdifference)


# a ^= b	Set a to contain the elements in either a or b but not both
symmetric_difference_update=a.symmetric_difference_update(b)
print(symmetric_difference_update)


# also built in sorted functions 
sorteds = sorted([2,5,6,4,2,4,9,1,23,5,4])
print(sorteds)
stringSorted = sorted('horse race')
print(stringSorted)