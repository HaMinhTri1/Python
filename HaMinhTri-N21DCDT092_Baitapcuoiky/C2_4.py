import array as arr
import numpy as np
from array import*
s = 0
np_arr = np.array([180,255],dtype='B')
for i  in range(len(np_arr)):
    s = s + np_arr[i]
    
print(s)