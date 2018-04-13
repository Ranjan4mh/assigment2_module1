import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df1=pd.read_csv("D:\diabetes.csv")
df1
df1.head()
df1.tail()
df1.describe()
x=df['Glucose']
y=df['BloodPressure']
z=df['Outcome']
o=df['']
plt.hist(x)
plt.hist(y)
plt.show()
plt.scatter(x,y)
plt.show()
df.corr()
colors={'yes':'red','no':'green'}
colors=['yes']
plt.scatter(x,y, c=z.apply(lambda x:colors[x]))
