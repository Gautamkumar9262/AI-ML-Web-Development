#slicing element from array.
#slice(start, stop, next)

import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr[1:4])
print(arr[::-1])
print(arr[:4])
print(arr[::2]) #1,3,5
print(arr[10]) #indexError overflow