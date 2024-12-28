import math 
 
x = 3.4
p = math.floor(x)
print(p)

# string formatting 
num1=15
num2=22
print(f"this si  super number {num1+num2}")

# immutable
lists = [11,22,33,44,56,66,77]
b = bytes(lists)
print(type(b))


# mutable array
list2= [11,22,33,44,56,66,77]
b1 = bytearray(list2)
b1[3] = 90

print(list(b1))
