import pandas as pd

data = {
    "Name": ["Gautam", "Dabbu", "Nitesh", "Raja", "Rohit", "Vikash", "Anmol"],
    "Age":[21,24,19,34,32,27,29],
    "Salary":[25000, 30000, 21000, 32000, 54000, 12000, 16000],
    "City":["Jaipur", "Delhi", "Patna", "Mumbai", "Kolkata", "Hydrabad","Gujrat"]
}
df = pd.DataFrame(data)
print(df)


df["Bonus"] = df["Salary"]*10/100
print(df)

#you can add column on specific column
df.insert(0, "Id", [101,102,103,104,105,106,107])
print(df)