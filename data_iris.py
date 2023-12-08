from sklearn.datasets import load_iris
import matplotlib.pyplot as plt


iris = load_iris(as_frame=True)
df = iris['data']
df['iris'] = iris['target']

print(df.columns)
print(df.shape)
print(df.describe())

colors = ['red', 'blue', 'green']
for i, flower in enumerate(df['iris'].unique()):
    temp = df.loc[df['iris']==flower]
    plt.scatter(x=temp['sepal length (cm)'].values,
                y=temp['petal length (cm)'].values,
                color=colors[i])

plt.show()

### Groupby ####
df_mean = df.groupby('iris').mean()  #mean, std, count, max, min, median skew
print(df_mean)

### filter
df_filtered = df.groupby('iris')['petal length (cm)'].filter(lambda x: x.mean()>3)
print(df_filtered)

### transform ###
df['petal length (cm)_mean'] = df.groupby('iris')['petal length (cm)'].transform('mean')  #mean, std, count, max, min, median

plt.plot(df['petal length (cm)'], label='petal length (cm)')
plt.plot(df['petal length (cm)_mean'], label='petal length (cm)_mean')
plt.legend()
plt.show()





