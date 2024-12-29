# zip “pairs” up the elements of a number of lists, tuples, or other sequences to create a list of tuples:
seq1 = ["foo", "bar", "baz"]
seq2 = ["one", "two", "three"]

zipped = zip(seq1,seq2)
tuples = tuple(zipped)
print(tuples)

