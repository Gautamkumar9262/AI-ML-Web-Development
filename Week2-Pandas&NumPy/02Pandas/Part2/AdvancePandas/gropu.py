import pandas as pd
data = {
    "marks":[12,45,12,90,23,67],
    "Age":[21,34,21,56,34,45],
    "Salary":[10000, 30000, 56000, 15000, 7000, 13000]
}

df = pd.DataFrame(data)
print(df)

groupedData = df.groupby(["Age","marks"])["Salary"].sum()
print(groupedData)