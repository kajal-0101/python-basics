'''
Asks the user for two integers, and then displays whether the second integer
is a divisor of the ﬁrst integer
'''


print("Two integers are to be taken as input")
a=input("Enter the first integer: ")
a=int(a)
b=input("Enter the second integer: ")
b=int(b)
if(a>b):
	large=a
	small=b
	print("The larger value is {} and the smaller value is {}".format(large,small))
else:
	large=b
	small=a
	print("The larger value is {} and the smaller value is {}".format(large,small))

mod=large%small
if(mod==0):
	print("The smaller value {} is a divisor of the larger value {}".format(small,large))
else:
	print("The smaller value {} is not a divisor of the larger value {}".format(small,large))