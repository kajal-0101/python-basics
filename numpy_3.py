'''
Create two-dimensional empty array
a. Append nine values starting from 15.
b. Shape of the array should be 3x3. (Qn: a&b in one line of code)
c. Slice the last three values from original array to make new array.
'''

import numpy as np
print("The original array is: ")
a = np.arange(15,24,1).reshape(3,3)
print(a)
row3 = a[2]
print("\nThe last three value of the original array are being made into another new array: ")
print (*row3, sep=" ", end="\n")
