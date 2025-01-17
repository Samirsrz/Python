import pandas as pd
bios = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/bios.csv')

# print(bios.head())
# print(bios.info())
#  filtering data
# print(bios.loc[bios['height_cm'] > 215, ['name', 'height_cm'] ])

# print(bios.loc[(bios['height_cm']>215) & (bios['born_country']=='USA')]) 

# print(bios.loc[bios['name'].str.contains("Tommy Quick"), ['name','height_cm']])

# print(bios.loc[bios['name'].str.contains(r'(.)\1',na=False), ['name']])

x = bios.loc[bios['born_country'].isin(["USA", "FRA", "GBR"]) & (bios["name"].str.startswith("Keith")), ['name']]

print(x)

