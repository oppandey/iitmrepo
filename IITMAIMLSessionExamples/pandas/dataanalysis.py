import pandas as pd
import numpy as np

df = pd.read_csv("D:\\P01_Learning Services\\DS DE Gen AI\\IITMAIMLSessionExamples\\sampledatasets\\products-1000.csv")

#df1 = df.groupby("Color").count()
#print(df1)
#print(df["Color"].skew)
#print(df["Color"].kurtosis)
#df1 = df["EAN"].kurtosis()
#print(df1)

df2 = df.groupby("Color").agg({"Price": "mean", "Stock": "sum"})
print(df2)