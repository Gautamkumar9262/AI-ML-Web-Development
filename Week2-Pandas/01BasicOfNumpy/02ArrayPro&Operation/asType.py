import numpy as np
arr = np.array([[1,2,3],[2,3,4]])

print(arr.dtype)
as_type = arr.astype(float)
print(arr)
print(as_type.dtype)
