import pandas as pd

data = {
    "Name": ["Gautam", None, "Nitesh", "Raja", "Rohit", "Vikash", "Anmol"],
    "Age":[21,None,19,34,32,27,29],
    "Salary":[25000, None, 21000, 32000, 54000, 12000, 16000],
    "City":["Jaipur", None, "Patna", "Mumbai", "Kolkata", "Hydrabad","Gujrat"]
}
df = pd.DataFrame(data)
print(df)

print(df.isnull())
print(df.isnull().sum())