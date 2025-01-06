import pandas as pd
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=["A","B","C"], index=["x","y","z"])
print(df)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())
print(df.shape)

