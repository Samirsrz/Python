import pandas as pd
import numpy as np

coffee = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')

# adding new column
coffee_new = coffee
coffee_new['price'] = 4.99
# print(coffee_new.head())

coffee['new_price'] =  np.where(coffee['Coffee Type'] == 'Espresso', 3.99, 5.99)
# print(coffee.head())

# to drop a column
coffee = coffee.drop(columns=['price'])


# revenue column
coffee['revenue'] = coffee['Units Sold'] * coffee['new_price']
# print(coffee.head())

# to rename
coffee = coffee.rename(columns={'new_price' : 'price'})
print(coffee.head())
