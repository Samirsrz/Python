all_data = [
    ["John", "Emily", "Michael", "Mary", "Steven"], ["Maria", "Juan", "Javier", "Natalia", "Pilar","Saamir"]
]

namesOfInterest = []

for names in all_data:
    enough_as = [name for name in names if name.count("a") >= 2]
    namesOfInterest.extend(enough_as)

print(namesOfInterest)

