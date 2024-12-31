all_data = [
    ["John", "Emily", "Michael", "Mary", "Steven"], ["Maria", "Juan", "Javier", "Natalia", "Pilar","Saamir"]
]

namesOfInterest = []

for names in all_data:
    enough_as = [name for name in names if name.count("a") >= 2]
    namesOfInterest.extend(enough_as)

print(namesOfInterest)

# Another problem to create it into a single list
tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flattened = []

for tup in tuples:
    for x in tup:
        flattened.append(x)


print(flattened)
