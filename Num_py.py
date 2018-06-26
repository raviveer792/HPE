'''import numpy,scipy
print(numpy.version.full_version)
print(scipy.version.full_version)
print(scipy.dot is numpy.dot)'''

import numpy as np
import numpy.core.records as ncr

'''a=np.array([0,9,8,7,6,5,4,3,2,1,2,1])
print(a)
print(ncr.array([0,9,3,4,5,6,7,3,4]))
print(a.ndim)
print("Shape: ",a.shape)
b=a.reshape(3,4)
print("Reshape: ",b)
b[1][1]=2
print("After Update Reshape: ",b)
print(a*2)
print(a**2)
print([0,9,8,7,6,5,4,3,2,1]*2)
print(a>4)'''

c = np.array([1, 2, np.NAN, 3, 4]) # let's pretend we have read this from a text file
#a=np.array([1,2,3,4,"Hii",3,5])
#print(np.isnan(a))
print(np.isnan(c))
print(~np.isnan(c)) # Form Reverse STatement



