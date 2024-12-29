words = ["apple", "bat", "bar", "atom", "book","cook", "dick"]
by_letter = {}
for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter]=[word]
    else:
        by_letter[letter].append(word)

print(by_letter)

# taking user input 
username =  input("Enter username")
print("the user name is "+ username)

#  string
# amra  hash er bhitore only immutable data type rakhte parbo jemon int,float,string, tuples as eta r change kora jayna
k = hash("This is it")
y =  hash((1,2, (3,4)))
print(k)

