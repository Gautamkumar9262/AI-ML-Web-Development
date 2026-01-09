import pandas as pd

data = {
    "Name": ["Gautam", "Dabbu", "Nitesh", "Raja", "Rohit", "Vikash", "Anmol"],
    "Age":[21,None,23,24,None,26,27],
    "Salary":[25000, None, 35000, 40000, 45000, 50000, 55000],
    "City":["Jaipur", "Delhi", "Patna", "Mumbai", "Kolkata", "Hydrabad","Gujrat"]
}
df = pd.DataFrame(data)
print(df)

print("Before interpolating ")
print(df)


print("After interpolating ")
df["Age"].interpolate(method="linear", inplace=True)
df["Salary"].interpolate(method="linear", inplace=True)
print(df)

