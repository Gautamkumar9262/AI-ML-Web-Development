import numpy as np

arr = np.array([1,2,3,4,5,6,np.inf, 8,9,-np.inf])
print(np.isinf(arr))

new_arr = np.nan_to_num(arr, posinf=10, neginf=-10)
print(new_arr)