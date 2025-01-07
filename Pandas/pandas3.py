import pandas as pd
#  loc function
coffee = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')

# # will print omly the 0,1,5 th rows
# print(coffee.loc[[0,1,5]])

# # we can also use filter 
# print(coffee.loc[4:8])

# # we can also select the columns we want to see
# print(coffee.iloc[0:5,[0,2]])

# # we can change the column if we want
# coffee.index = coffee["Day"]
# print(coffee.head())

# now if we want to filter , we cant use .loc[0:5] as no more index is there now we have replaced it with Days so to filter we can use names of the Days eg Monday
print(coffee.loc["Monday":"Wednesday"])

# we can also change values
coffee.loc[1, "Units Sold"] = 10
print(coffee.loc[[0]])


print(coffee.Day) 

# to sort
# print(coffee.sort_values("Units Sold"))
print("SOrted using two columns")
print(coffee.sort_values(by=["Units Sold", "Coffee Type"]))