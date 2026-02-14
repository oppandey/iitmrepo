#import numpy as np
#import pandas as pd

# NumPy Array
#arr = np.array([10, 20, 30])
#print(arr[1])  # Access by position

# Pandas Series - Pandas are built on top of NumPy and provide more functionality
#ser = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
#print(ser['b'])  # Access by label

import pandas as pd
import json

ages = pd.Series([10, 20, 30, 40])
#print(ages)

#using DataFrame
df = pd.DataFrame(
    {
        "Names":["Ganesh","Mahesh","Dinesh"],
        "Salary":[3234234,575677,4645454]
     })
#print(df.head())
#print(df.columns)
df = df.sort_values("Salary")
print(df)
sum = df["Salary"].sum()
print(sum)
first_sal = df["Salary"][0]
print(first_sal)

#loading data from csv
df = pd.read_csv("D:\\P01_Learning Services\\DS DE Gen AI\\IITMAIMLSessionExamples\\sampledatasets\\products-1000.csv")
print(df.head())

#create customer details using json
customer_data = [
    {"CustomerID": 1, "Name": "Alice", "Email": "alice@example.com"},
    {"CustomerID": 2, "Name": "Bob", "Email": "bob@example.com"},
    {"CustomerID": 3, "Name": "Charlie", "Email": "charlie@example.com"}
]

#df_customers = pd.read_json("D:\\P01_Learning Services\\DS DE Gen AI\\IITMAIMLSessionExamples\\sampledatasets\\myfile.json")
df_customers = pd.DataFrame(customer_data)
print(df_customers) 

data = {"One": {"0": 60, "1": 60, "2": 60, "3": 45, "4": 45, "5": 60},
        "Two": {"0": 110, "1": 117, "2": 103, "3": 109, "4": 117, "5": 102}}

json_data = json.dumps(data)

df_normalize = pd.json_normalize(json.loads(json_data))
print("\nDataFrame using JSON module and `pd.json_normalize()` method:")
print(df_normalize)
print(df_customers.shape)
print(df_customers.info)
print(df.describe)