import pandas as pd
import numpy as np

d = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}
df = pd.DataFrame(d)

mv = df.isnull()

print(mv)

d = pd.read_csv("employees.csv")

bool_series = pd.isnull(d["Gender"])
missing_gender_data = d[bool_series]
print(missing_gender_data)


#data = pd.read_csv("employees.csv")
#d[10:25]
#d["Gender"].fillna('No Gender', inplace = True) 
#print(d[10:25])

#data = pd.read_csv("employees.csv")
#data[10:25]
#data = data.replace(to_replace=np.nan, value=-99)
#print(data[10:25])

