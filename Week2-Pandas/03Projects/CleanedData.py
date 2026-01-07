import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\gauta\OneDrive\Desktop\AI-ML&Web-Jan_Goal\Week2-Pandas\03Projects\MOCK_DATA (1).csv")

print("************************************************************* Top 5 Data From DataSet*****************************************************")
print("==========================================================================================================================================")
print(df.head())
print("==========================================================================================================================================")


print("===========================")
print("Missing Data in Dataset")
print("===========================")
print(df.isnull().sum())

df['Salary'].fillna(df["Salary"].mean(), inplace=True)
df['Experience (Year)'].fillna(df["Experience (Year)"].mean(), inplace=True)
df['Performance Rating'].fillna(df["Performance Rating"].mean(), inplace=True)

print("===========================")
print("After fill Missing Data in Dataset")
print("===========================")
print(df.isnull().sum())

df.to_csv("Cleaned_Employees_Data.csv", index=False)
print('Data cleaning completed ! "Save as Cleaned_Employees_Data.csv" ')