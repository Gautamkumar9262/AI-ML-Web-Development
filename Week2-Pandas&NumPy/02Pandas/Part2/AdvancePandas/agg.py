#Aggregation of data

import pandas as pd
data = {
    "marks":[12,45,33,90,23,67],
    "Salary":[10000, 30000, 56000, 15000, 7000, 13000]
}

df = pd.DataFrame(data)
print(df)

print("Average Salary: ",df["Salary"].mean())

print("Max Salary: ",df["Salary"].max())

print("Min Salary: ",df["Salary"].min())

print("STD Salary: ",df["Salary"].std())

print("Varience Salary: ",df["Salary"].var())

print("Sum of Salary: ", df["Salary"].sum())