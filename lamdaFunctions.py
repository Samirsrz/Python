
# lamda functions are functions jeta amra pore banay dite parbo first e just f likhte rakhte pari
def apply_list(some_list, f):
    return [f(x) for x in some_list]

ints = [2,4,6,8,10]

listed = apply_list(ints, lambda x: x/2)
print(listed)

# example 2 
# number of unique characters onujay print kora hoise
strings = ["foo", "card", "bar", "aaaa", "abab"]

strings.sort(key=lambda x: len(set(x)))

print(strings)

# ekhane shob gular unique characters r oigular length print kortesi
for x in strings:
    unique_characters = set(x)
    print(f"String: {x} , Unique characters : {unique_characters}, count:{len(unique_characters)}")


dictionary = {"a": 44, "b": [1,2,3], 5: "some letters"}


