#.ravel()  -> view
#.flatten() -> copy

import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8]])
# print(arr)
print(arr.flatten()) #[1,2,3,4,5,6,7,8]
# print(arr.ravel()) #[1,2,3,4,5,6,7,8]
# print(arr)
