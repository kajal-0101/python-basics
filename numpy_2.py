'''
Write a Python program using NumPy to generate 1x3 dimensional array with random
values. From the generated array of values do the following operations.
a. Find the square root of each values and make a new array from it.
b. Concatenate original array and square root array.
c. Count and display number of even and odd values from concatenated array.
'''

import numpy as np
a = np.random.randint(low=3,high=5,size=(3))
print("The original array is:")
print(a)
b=np.sqrt(a)
print("\nThe square root of the value of the original array: ")
print(b)
c = np.append(a,b,axis=0)
print("\nThe concatinated arrays are: ")
print(c)
even = []
odd =[]
for i in range(0,len(c)):
    if(c[i]%2 == 0):
        even.append(c[i])
    else:
        odd.append(c[i])
print("\nThe no. of even numbers in the concatenated array: ", len(even))
print("\nThe even numbers are: ")
print(even)
print("\nThe no. of odd numbers in the concatenated array: ", len(odd))
print("\nThe odd numbers are: ")
print(odd)
