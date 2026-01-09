import pandas as pd
data = {
    "marks":[12,45,33,90,23,67],
    "Salary":[10000, 30000, 56000, 15000, 7000, 13000]
}

df = pd.DataFrame(data)
print(df)

#Single column sorting
df.sort_values(by="marks", ascending=True, inplace=True)
print(df)


#Multiple column sorting
df.sort_values(by=["marks", "Salary"], ascending=[True, True], inplace=True)