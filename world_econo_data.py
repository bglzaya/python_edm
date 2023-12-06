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

### merge data
df_merged = None

for file in files:
    df = pd.read_csv(f'data/{file}')
    if df_merged is None:
        df_merged = df
    else:
        df_merged = df_merged.merge(df, on=['country'], how="left", copy=False)

print(df_merged.head())

## missing values
for col in df_merged.columns:
    print(col, df_merged[col].isnull().sum())