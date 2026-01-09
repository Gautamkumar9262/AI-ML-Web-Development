import pandas as pd

data = {
    "Name": ["Gautam","Dabbu", "Nitesh", "Raja", "Rohit", "Vikash", "Anmol"],
    "Age":[21,None,19,34,32,27,29],
    "Salary":[25000, None, 21000, 32000, 54000, 12000, 16000],
    "City":["Jaipur", "Delhi", "Patna", "Mumbai", "Kolkata", "Hydrabad","Gujrat"]
}
df = pd.DataFrame(data)
print(df)

df.interpolate(method="linear", axis=0, inplace=True)
print(df)