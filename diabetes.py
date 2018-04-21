import numpy as np
import pandas as pd
import seaborn as sns
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
x=df['Glucose']
y=df['BMI']
z=df['Outcome']
#Histogram for x,y
plt.hist(x)
plt.show()
plt.hist(y)
plt.show()
#2 variable Scattered diagram for X,Y
plt.scatter(x,y)
plt.show()
#Co relation Matrix 
df.corr()
#Adding Colors
colors={1:'red',0:'green'}
#Getting color to the scattered graphs
plt.scatter(x,y, c=z.apply(lambda x:colors[x]))
plt.xlabel('Glucose')
plt.ylabel('BMI')
plt.show()

train,validate,test = np.split(df.sample(frac=1),[int(.6*len(df)), int(.8*len(df))]) 
train
train.describe()
train.corr()
plt.hist(train.Glucose)
plt.hist(train.BMI)
validate
validate.describe()
validate.corr()
plt.hist(validate.Glucose)
plt.hist(validate.BMI)
test
test.describe()
test.corr()
plt.hist(test.Glucose)
plt.hist(test.BMI)
sns.set(style="darkgrid", color_codes="true")
sns.FacetGrid(df,  size=5 ).map(plt.scatter,"Glucose","BMI").add_legend()
sns.jointplot(x="Glucose",y="BMI",data=df,size=7)
sns.boxplot(x="Outcome",y="BMI",data=df)
plt.show()
sns.boxplot(x="Outcome",y="Glucose",data=df)
plt.show()
sns.boxplot(x="Outcome",y="Glucose",data=df)
sns.stripplot(x="Outcome",y="Glucose",jitter=True,data=df)
plt.show()
sns.pairplot(df,hue="class", size=5)
train ,test=np.split(df.sample(frac=1),[int(.7*len(df))])
train
test
df.boxplot(by="Outcome",figsize=(12,10))
sns.FacetGrid(df,size=6).map(sns.kdeplot,"Glucose").add_legend()

#Joint Plot
sns.jointplot(x="Glucose",y="BMI",data=df,size=5)

#Bin Variables after Rules are discovered 
#Rule 1: Outcome is 1 if 30<BMI<=40
#Rule 2: Outcome is 1 if 120<Glucose<=170
df['BMIBin'] = np.where(df['BMI'] <30,'<30', (np.where(df['BMI'] >= 40 ,'>=40','30-40')))
df['GlucoseBin'] = np.where(df['Glucose'] <120,'<120', (np.where(df['Glucose'] >= 170 ,'>=170','120-170')))

#create Pivot Table on training data
pd.pivot_table(train, values="BMI", index=["BMIBin"], columns="Outcome", aggfunc = "count",fill_value=0)
pd.pivot_table(train, values="Glucose", index=["GlucoseBin"], columns="Outcome", aggfunc = "count",fill_value=0)

#create Pivot Table on test data
pd.pivot_table(test, values="BMI", index=["BMIBin"], columns="Outcome", aggfunc = "count",fill_value=0)
pd.pivot_table(test, values="Glucose", index=["GlucoseBin"], columns="Outcome", aggfunc = "count",fill_value=0)