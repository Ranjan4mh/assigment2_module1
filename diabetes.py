import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Reading CSV from file system.
df=pd.read_csv("D:\diabetes.csv")
df
#Getting Top 5 element of the Excel data.
df.head()
#Getting Bottom 5 element of the Excel data.
df.tail()
#Getting Mean Median and mode and description.
df.describe()
#Created 3 Variables x,y,z
x=df['Pregnancies']
y=df['SkinThickness']
z=df['Outcome']
#Histogram for x,y
plt.hist(x)
plt.hist(y)
plt.show()
#2 variable Scattered diagram for X,Y
plt.scatter(x,y)
plt.show()
#Co relation Matrix 
df.corr()

colors={'yes':'red','no':'green'}
colors=['yes']
plt.scatter(x,y, c=z.apply(lambda x:colors[x]))