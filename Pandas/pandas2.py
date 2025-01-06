import pandas as pd

coffee = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')

# first 5 rows
print(coffee.head())
# all rows
print(coffee)
# last 5
print(coffee.tail(6))
# too large data
# results = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/results.csv')

 # print(results.head())

