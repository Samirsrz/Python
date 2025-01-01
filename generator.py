def squares(n=10):
    print(f"Generating squares from 1 to {n ** 2}")
    for i in range(1, n+1):
        yield i**2


gen = squares()

print(gen)

for x in gen :
    print(x, end="")


cubics = (x**2 for x in range(10))
print(list(cubics))

# filter and transform data 
names = ["Sam", "Eve", "John", "Alice", "Bob"]
filtered_names = (name.upper() for name in names if len(name) > 3)

for name in filtered_names:
    print(name)