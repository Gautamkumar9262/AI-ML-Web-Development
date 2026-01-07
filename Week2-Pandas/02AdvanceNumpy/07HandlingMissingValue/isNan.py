import numpy as np

arr = np.array([1,2,3,4,5,np.nan,6,])

print(np.isnan(arr))

#not compare with nan - nan

print(np.nan == np.nan) 
