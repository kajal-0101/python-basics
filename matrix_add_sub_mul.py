'''
Write a program to perform matrix addition, subtraction, multiplication
'''
import numpy as np
print("Program to perform matrix addition, subtraction, multiplication")
print("Enter the details of matrix 1")
r1 = int(input("Enter the no. of rows for matrix 1: "))
c1 = int(input("Enter the no. of columns for matrix 1: "))
print("Enter the entries row-wise in a single line")
e = list(map(int, input().split()))
m1 = np.array(e).reshape(r1, c1)
print(m1)
print("Enter the details of matrix 2")
r2 = int(input("Enter the no. of rows for matrix 2: "))
c2 = int(input("Enter the no. of columns for matrix 2: "))
print("Enter the entries row-wise in a single line")
e = list(map(int, input().split()))
m2 = np.array(e).reshape(r2, c2)
print(m2)
print("\nMatrix Addition: ")
if(r1 == r2 and c1 == c2):
 print("Matrix addition is possible")
 result = np.add(m1,m2)
 print(result)
else:
 print("Matrix addition not possible")
print("\nMatrix Subtraction: ")
if(r1 == r2 and c1 == c2):
 print("Matrix subtraction is possible")
 result1 = np.subtract(m1,m2)
 print(result1)
else:
 print("Matrix subtraction not possible")
print("\nMatrix Multiplication: ")
if(r2 == c1):
 print("Matrix multiplication is possible")
 result2 = np.dot(m1,m2)
 print(result2)
else:
 print("Matrix multiplication is not possible")