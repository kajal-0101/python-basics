'''
Write a Python program using NumPy to generate array of random values.
a. Find the length of the array
b. Search and print the repeated value in an array.
c. Sort the values in an array
d. Find the min, max, mean, median from an array of values.
'''

import numpy as np
a = np.array([[1,2,3],[3,4,2],[3,5,4]])
print("The original array is: ")
print(a)
print("\nThe shape of the array is: ", a.size)
b = np.sort(a, axis=-1)
print("Sorting the array row-wise: ")
print(b)
print("The min value of the array is: ",np.min(a))
print("The max value of the array is: ",np.max(a))
print("The mean of the elements of the array is: ",np.mean(a))
print("The median of the elements of the array is: ",np.median(a))
uni=np.unique(a)
print("The unique elements in the array are: ")
print(uni)
