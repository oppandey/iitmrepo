from scipy import stats
import pandas as pd
import numpy as np

d = pd.read_csv("employees.csv")
zscores = stats.zscore(d["Salary"])
#print(zscores)

print(d["Gender"].value_counts())
print(d["Gender"].value_counts(normalize=True))