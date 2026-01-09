import pandas as pd

data = {
    "Name":["Gautam Kumar"],
    "Age":[21],
    "City":["Jaipur"]
}

df = pd.DataFrame(data)
print(df)

df.to_csv("Data.csv", index=False)