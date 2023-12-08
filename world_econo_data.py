import pandas as pd
import matplotlib.pyplot as plt

files = ['corruption.csv',
         'cost_of_living.csv',
         'richest_countries.csv',
         'tourism.csv',
         'unemployment.csv']

for file in files:
    df = pd.read_csv(f'data/{file}')
    print(f'Data {file}:', list(df.columns))

#data concat examples
df1 = pd.read_csv(f'data/{files[0]}')
df2 = pd.read_csv(f'data/{files[1]}')

print('data 1:', df1.shape)
print('data 2:', df2.shape)

df_axis0 = pd.concat([df1, df2], axis=0)
df_axis1 = pd.concat([df1, df2], axis=1)

print(df_axis0.shape)
print(df_axis0.columns)
for col in df_axis0.columns:
    print(col, df_axis0[col].isnull().sum())

print()
print(df_axis1.shape)
print(df_axis1.columns)
for col in df_axis1.columns:
    print(col, df_axis1[col].isnull().sum())

print(df_axis1["country"])  #wrongly concat


### merge data
df_merged = None

for file in files[:2]:
    df = pd.read_csv(f'data/{file}')
    # print()
    # print(file)
    # print(df.shape)
    # print(df.describe())
    if df_merged is None:
        df_merged = df
    else:
        df_merged = df_merged.merge(df, on=['country'], how="left", copy=False)

print()
print(df_merged.shape)
print(df_merged.columns)
for col in df_merged.columns:
    print(col, df_merged[col].isnull().sum())

print(df_merged) #correctly merged 


###
print(df_merged.head())

## missing values
for col in df_merged.columns:
    print(col, df_merged[col].isnull().sum())