'''
Write a Python program using NumPy to generate two arrays of same dimensions and perform the arithmetic operations implemented in NumPy. 
Similarly perform following actions and print the result values,
a. Search and print the repeated value in an array.
b. Sort the values in an array
c. Find the min, max, mean from an array of values.
'''

import numpy as np
#==============Declaring the arrays====================
a = np.array([[2,3,4],[5,2,3],[7,6,5]])
print("The first array is: ")
print(a)
b = np.array([[7,8,5],[8,6,4],[4,5,2]])
print("\nThe second array is: ")
print(b)
#================Addition of two arrays=================
print("\nThe sum of the first two arrays is: ")
c=np.add(a,b)
print(c)
#===============Search and print the repeated value in an array=====================
print("\nPrinting the unique elements and their frquency:")
print("First Array:")
au,ac=np.unique(a,return_counts=True)
print(np.asarray((au,ac)))
print("\nSecond Array:")
bu,bc=np.unique(b,return_counts=True)
print(np.asarray((bu,bc)))
print("\nResultant Array:")
ru,rc=np.unique(c,return_counts=True)
print(np.asarray((ru,rc)))
#================Sorting the arrays=====================
print("\nSorting the first array: ")
a=np.sort(a, axis=1)
print(a)
print("\nSorting the second array: ")
b=np.sort(b, axis=1)
print(b)
print("\nSorting the resultant array: ")
c=np.sort(c, axis=1)
print(c)
#================Finding maximum value from the array=======================
print("\nThe max value of first array is: ", np.max(a))
print("The max value of second array is: ", np.max(b))
print("The max value of resultant array is: ", np.max(c))
#===============Finding minimum value from the array========================
print("\nThe min value of first array is: ", np.min(a))
print("The min value of second array is: ", np.min(b))
print("The min value of resultant array is: ", np.min(c))
#==============Finding mean value from the array============================
print("\nThe mean value of first array is: ", np.mean(a))
print("The mean value of first array is: ", np.mean(b))
print("The mean value of first array is: ", np.mean(c))
