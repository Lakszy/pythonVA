import numpy as np
from numpy import *

arr=array([1,2,3,4,5,6,7],float)
print(arr)
print(arr.dtype)

larr=linspace(0,15,16)
# means 0 -15 in 16parts
print(larr )


karr=arange(1,15,2)
# 1 3 5 7 9 11 13
print(karr )

 
arr1=array([1,123,45,6,7,8])
arr2=array([1,123,45,6,7,8])
arr3=arr1+arr2
print(arr3)
print(sqrt(arr3))
print(log(arr3))



# multidimension


arrl=array([
          [1,2,3,4,56,7,8],
          [12,12,23,47,56,78,98]
])

print(arrl)
print(arrl.ndim)
print(arrl.shape)#dimension

#2d to 1d
arrf=arrl.flatten()
print(arrf)

# 2d to 3d
arrf = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arrt = arrf.reshape(2,2,3)
print(arrt)


# flatten the array
# flat_list = [item for sublist in l for item in sublist]

# flat_list = []
# for sublist in l:
#     for item in sublist:
#         flat_list.append(item)

# def flatten(l):
#     return [item for sublist in l for item in sublist]



print("---------------")
m1=matrix('1 2 3; 6 4 5 ; 1 6  7')
m2=matrix('11 12 13; 16 14 15 ; 11 16 17')
m3=m1*m2
print(m3)