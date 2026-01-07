#solution - without loop
import numpy as np

price = np.array([100,200,300,400])

finalPrice = price - price*10/100
print(finalPrice)