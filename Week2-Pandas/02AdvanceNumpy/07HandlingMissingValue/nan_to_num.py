import numpy as np
arr = np.array([10,20,np.nan, 60,100,np.nan])

print(arr)
print(np.isnan(arr))

mean_value = arr.max
new_arr = np.nan_to_num(arr,nan=100)

print("After fill measing value")
print(new_arr)
