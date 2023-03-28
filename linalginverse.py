# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:40:27 2023

@author: Kairu Cyrus
"""

# Finding the inverse of a matrix
#We use the numpy function linalg.inv()
# Given a matrix A, the inverse of the matrix, A^-1 multiplied with the original matrix gives an identity matrix

#python arrays are best for matrix operations
import numpy as np
m1 = np.array([[4,10,14], [9,7,11], [8,6,18]])
m2 = np.linalg.inv(m1)
print(f"m2: {m2}")

#remember that singular matrices are an exception since their determinants are zero.
#therefore, it is recommended to use the function in a try and except block 
# This function raises an error if the matrix inverse is not possible, which can because the matrix is singular
import numpy as np
try:
    mt1 = np.array([[4,10,14], [9,7,11], [8,6,18]])
    mt2 = np.linalg.inv(mt1)
    print(f"mt2 : {mt2}")
except:
    print("Singular matrix, inverse not possible.")

    #we can also use scipy module
import numpy as np
from scipy import linalg
try: 
    mr1 = np.matrix([[4,10,14], [9,7,11], [8,6,18]])
    print(f"mr2: {linalg.inv(mr1)}")
except:
    print("Singular matrix, inverse not possible")

 