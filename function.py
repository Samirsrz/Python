def addition(x,y):
    return x + y

a = 5 
b = 6

result = addition(a,b)
print(result)

# re library functions 

import re
states = ["   Alabama ", "Georgia!", "Georgia", "georgia", "FlOrIda", "south   carolina##", "West virginia?"]

def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub("[!#?]", "", value)
        value = value.title()
        result.append(value)
        return result
    

print(clean_strings(states))
