import pandas as pd

df = pd.DataFrame({
        "EmpId":[1001, 1002],
        "EmpName":["ABC","PQR"],
        "CTC":[132342, 242342]
    }
)
#print(df)

employeesdata = pd.read_csv("employees.csv")
print(employeesdata)