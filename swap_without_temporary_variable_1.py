'''
Write a program with a function to swap two numbers without using temporary variables.
'''
def swap(num1, num2):
 print("\nInput: num1 = {} and num2 = {}".format(num1, num2))
 num1 = num1 + num2
 num2 = num1 - num2
 num1 = num1 - num2
 print("Output: num1 = {} and num2 = {}".format(num1, num2))

print("Swapping numbers without using temporary variables")
swap(5,6)
swap(4,3)