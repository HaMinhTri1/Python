import numpy as np
from array import*
arr1= array('i', [1,2,3,4])

print(arr1)
arr1.insert(6,9) #them phan tu vao mang
print(arr1)
def traverseArray(array):
    for i in array:
        print(i)
traverseArray(arr1)
def accessE(array, index):
    if index > len(array):
        print('there is not any element in this index')
    else:
        print('The value of array index: ',array[index])
accessE(arr1,2)
arr1.append(7)
print(arr1)

