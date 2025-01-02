even_sum = sum(x for x in range(100) if x%2 == 0)
print(even_sum)

# Find the Product of All Odd Numbers in a List
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
product = 1
for n in (num for num in nums if num%2!=0 ):
    product *= n
print(product)


# fibonacci
def fibonacci():
    a ,b = 0,1
    while True:
        yield a 
        a,b = b, a+b

fir_gen = (y for _, y in zip(range(10), fibonacci()))
print(list(fir_gen))


# -------------------------------------

items_with_square = dict((i, i**2) for i in range(5))
print(items_with_square)
