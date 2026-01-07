#2d array insertion

import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr)

insert_ele = np.insert(arr, 2, [7,8,9], axis=0) #rows
print(insert_ele)

insert_ele2 = np.insert(insert_ele, 0, [1,1,1], axis=None) #columns
print(insert_ele2)