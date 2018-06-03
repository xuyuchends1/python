import numpy as np

data1=[6,7.5,8,0,1]
arr1=np.array(data1)
print (arr1)
data2=[[1,2,3,4],[5,6,7,8]]
arr2=np.array(data2)
print(arr2)
print(arr2.ndim)
print(arr2.shape)
print(np.asarray(data1))
print(np.zeros((2,4)))
print(np.zeros_like(data2))
print(np.eye(5))
print(np.identity(5))
np.sort