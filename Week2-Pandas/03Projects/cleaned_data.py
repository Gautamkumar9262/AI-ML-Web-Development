import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\gauta\OneDrive\Desktop\AI-ML&Web-Jan_Goal\Week2-Pandas\03Projects\employment_data.csv")

print(df.head())

print(df.isnull().sum())