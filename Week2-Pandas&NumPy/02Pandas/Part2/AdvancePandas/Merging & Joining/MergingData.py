import pandas as pd
customer_Details = {
    "customer_Id" : [1,2,3,4],
    "Cutomer_Name":["Gautam", "Nitesh", "Dabbu", "Raj"]
}

customer_Order_detail = {
    "customer_Id" : [1,2,3,5],
    "OderAmt":[450, 500, 430, 499]
}

cust = pd.DataFrame(customer_Details)
order = pd.DataFrame(customer_Order_detail)

print("Before merging Data", cust, "\n=================================================\n", order)

print("\n============After Inner Merging Data=============")
merged = pd.merge(cust, order, on="customer_Id", how="inner")
print(merged)

print("\n============After Outer Merging Data=============")
merged2 = pd.merge(cust, order, on="customer_Id", how="outer")
print(merged2)

print("\n============After Left Merging Data=============")
merged3 = pd.merge(cust, order, on="customer_Id", how="left")
print(merged3)

print("\n============After Right Merging Data=============")
merged4 = pd.merge(cust, order, on="customer_Id", how="right")
print(merged4)
