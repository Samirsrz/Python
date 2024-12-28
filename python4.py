tup = tuple(['foo', [1,2], True])
tup[1].append(3)

print(tup)

# swapping 
a,b = 1,3
print(a,b)
b,a=a,b
print(a ,b)

# another example of tuples in list

seq = [(1,2,3),(4,5,6),(7,8,9)]

for x,y,z in seq :
    print(f"a = {x}, b={y}, c= {z}")
    #  output  1,2,3 
    #          4,5,6 
    #          7,8,9


values = 1,2,3,5,7
m,n,*rest = values
print(m,n, rest)
# output m,n = 1,2 rest = [3,5,7]

 
