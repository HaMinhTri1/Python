import numpy as np
mystring = "1, 2, 3"
myarray = np.fromstring(mystring, dtype = int, sep = "," )
myarray= myarray.append(4)
print(myarray)