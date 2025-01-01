def apply_list(some_list, f):
    return [f(x) for x in some_list]

ints = [2,4,6,8,10]

listed = apply_list(ints, lambda x: x/2)
print(listed)
