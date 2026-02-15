import pandas as pd
import numpy as np

df = pd.read_csv("D:\\P01_Learning Services\\DS DE Gen AI\\IITMAIMLSessionExamples\\sampledatasets\\dirtydataset\\my_file.csv")

#print(df.info())
#print(df.describe())
df["Actual gross"] = df["Actual gross"].str.replace("$", "")
df["Actual gross"] = df["Actual gross"].str.replace(",", "")
df["Actual gross"] = df["Actual gross"].str.replace("[b]","")
df["Actual gross"] = df["Actual gross"].str.replace("[e]","")

#print(df["Actual gross"])
df1 = df["Actual gross"].astype(float)
#print(df1.sum)

#print(df.duplicated().sum())
#df["Year(s)"] = df["Year(s)"].str.replace("â€“", "-")
#print(df["Year(s)"])

print(df["Artist"].duplicated().sum())
#print(df.isnull().sum())
#print(df.dtypes)
#print(df.columns)
#print(df.shape)
#print(df.head())

#print(df["Age"].unique())
#print(df["Age"].value_counts())

print(df["Peak"].isnull().sum())

#df1 = df.dropna()
#print(df1)

#df2 = df.fillna(0)
#print(df2)

#df3 = df.replace(to_replace=np.nan, value=-99)
#print(df3)

#df4 = df.groupby("Artist").mean()
#print(df4)

# Calculate IQR bounds
#Q1 = df1.quantile(0.25)
#Q3 = df1.quantile(0.75)
#IQR = Q3 - Q1
#lower = Q1 - 1.5 * IQR
#upper = Q3 + 1.5 * IQR

# Find outliers
#outliers = df1[(df1 < lower) | (df1 > upper)]

#print(outliers)
print(df1.skew())
print(df1.kurt())
