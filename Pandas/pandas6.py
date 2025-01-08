import pandas as pd
bios = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/bios.csv')

bios_new = bios.copy()

bios_new['first_name'] = bios['name'].str.split(' ').str[0]
# print(bios_new[['name', 'first_name']])

# print(bios_new.query('first_name == "Keith"'))

# print(bios_new.info())

bios_new['born_datetime'] = pd.to_datetime(bios_new['born_date'])
print(bios_new.info())
