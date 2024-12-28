m=0
tup = ("samir","abir","rokinb","asasaaaaa","aaaaaaaaaaaaaa")
# list banay tuple ta ke b_list er moddhe rakhtese
b_list = list(tup)
print(b_list)
b_list[0] = "ehsan"
print(b_list)
# insert method aro method ase jemon append  
b_list.insert(2,"asif")
print(b_list)

# pop kore remove kore disi
print(b_list.pop(0))
# asif baade print hoise
print(b_list)

x = "asif" in  b_list
print(x)


tup2 = tuple(b_list)
print(tup2)

a_list = [2, 3, 7, None]
# extend kore list er size barateo pari

a_list.extend(["samir","amir"])
print(a_list)

# sort functions a_list.sort() likhlei shob sort hoye jabe
b_list.sort(key=len)
print("printing and sorting b-list according the length")
print(b_list)


# we can also use a[1:5] to print the elements between 1-5 index

a = [3,4,5,6,7,10,98,91,55]
print(a[1:4])
# last er 4ta jodi print korate chai
print(a[-4:])
print(a[:4])
print('Double colon')
# pichon theke ekta gap diye diye [55,98,7,5,3]
print(a[::-2])

