#problem  - loop  for n 

prices = [100,200,300,400]
discount = 10

newList = []

for price in prices:
    filnaPrice = price - price*10/100
    newList.append(filnaPrice)

print(newList)