import pandas as pd

region1 = pd.DataFrame(data={
    "Cust_Id":[1,2,3,4],
    "Cus_name":["Gautam","Dabbu", "Nitesh", "Raja"],
})

region2 = pd.DataFrame(data={
    "Cust_Id":[5,6,7],
    "Cus_name":["Baburao", "Motilal", "Chukiya"]
})

concta_Data = pd.concat([region1, region2], axis=0, ignore_index=True)
print(concta_Data)