import numpy as np

arr = np.array([[1,2,3,4,5],[6,7,8,9,0]])

print(arr)

#after removing item from array

new_arr = np.delete(arr, 1, axis=1)
print(new_arr)