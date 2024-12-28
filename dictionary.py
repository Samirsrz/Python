empty_dict = {}
# A dictionary stores a collection of key-value pairs, where key and value are Python objects. Each key is associated with a value so that a value can be conveniently retrieved, inserted, modified, or deleted given a particular key. One approach for creating a dictionary is to use curly braces {} and colons to separate keys and values:
d1 = {"a" : "some value", 'b' : [8,5,9,4]}
print(d1)

# to insert
d1[5] ="an integer"
print(d1)
d1["c"] = [11,22,33]
d1["b"].sort()
print(d1)
k =  11 in d1["c"]
print(k)

# to delete from d1 use del or we can use pop too
del d1['c'] 
d1.pop(5)
print("after deleting")
print(d1)

# if you want to print the keys of a dictionary use list(d1.keys()) or list(d1.values())

keys = list(d1.keys())
print(keys)

# if you want to print the list with its items 
d1[9] = "soem more values"
item_list = list(d1.items())
print(item_list)

# suppose if we want to update d1["a"]
d1.update({"a" : "updated using d1 update", "b" : 55})
print(d1)