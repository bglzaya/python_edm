import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 500)

import warnings


### read excel
file_path = 'data/labor_15.xlsx'
xls = pd.ExcelFile(file_path)
print('sheet names:', xls.sheet_names)

## read sheet
df =  pd.read_excel(file_path,
                    sheet_name='Data',
                    skiprows=[0])

print('Read data...', df)

df.columns = [str(x).lower() for x in df.columns]
#df['Статистик үзүүлэлт'] = df['Статистик үзүүлэлт'].apply(lambda x: x.lower())


### columns
cols = list(df.columns)

# for col in cols[:2]:
#     print("*"*10, col, "*"*10)
#     for val in df[col].unique():
#         print(val)

df_sub = df.loc[df[cols[1]]=='Ажилгүйдлийн түвшин, %']

df_sub['avg'] = df_sub[cols[-4:]].mean(axis=1)
print(df_sub[[cols[0], 'avg']])

# column selection
#indicators = df['Үзүүлэлт']

df[cols[-4]].plot()
plt.show()


