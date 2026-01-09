import pandas as pd
df = pd.read_csv(r"C:\Users\gauta\OneDrive\Desktop\AI-ML&Web-Jan_Goal\Week2-Pandas&NumPy\02Pandas\Part1\ShopEase_Sales.csv")

# print(df.head())

Jaipur_salse = df[df["City"]=="Jaipur"]

print(Jaipur_salse)

filteredData = df[(df["City"]=="Jaipur") & (df["Category"] == "Home")]
print(filteredData)

filteredData2 = df[(df["City"]=="Jaipur") & (df["Category"] == "Home") | (df["Payment_Method"]=="UPI")]
print(filteredData2)