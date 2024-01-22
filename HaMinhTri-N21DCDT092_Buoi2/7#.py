# remove element by remove and pop
import array as arr
from array import *
arr1= arr.array('i',[1,2,3,2,3,2,1,4,6,9])
arr1.remove(3) 
print(arr1) # xoa gia tri trong mang
print("Remove by pop method")
arr1.pop(3)
print(arr1)# xoa vi tri trong mang
# tim vi tri trong mang bang index method
index = arr1.index(2)
print('The index of 2: ',index)
#dao nguoc mang bang reverse method:
arr1.reverse()
print(arr1)
#Buffer_info array
bufferin = arr1.buffer_info()# hien thi thong tin bo nho dem
print(bufferin)
#dem so lan phan tu giong nhau xuat hien trong mang
c=arr1.count(2)
print("So lan so 2 xuat hien la: ",c)
#tostring ham tótring doi sang tobytes tu ban python 3.9
tostr = arr1.tobytes()
print(tostr)
#tolist
l=arr1.tolist()
print(l)
