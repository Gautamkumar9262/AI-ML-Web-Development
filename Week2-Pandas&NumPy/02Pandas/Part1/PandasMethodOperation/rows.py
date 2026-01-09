import pandas as pd

df = pd.read_csv(r"C:\Users\gauta\OneDrive\Desktop\AI-ML&Web-Jan_Goal\Week2-Pandas&NumPy\02Pandas\Part1\ShopEase_Sales.csv")
print(df.head())
print(df.tail())
print(df.isnull().sum())
