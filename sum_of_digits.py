'''
1) Asks the user for an integer, and then displays the sum of all the digits
'''

print("This program finds the sum of the digits of the entered integer")
s=0
n=int(input("Enter the integer: "))
print("The entered integer is {}".format(n))
temp=n
while(temp>0):
	a=temp%10
	temp=int(temp/10)
	print("The digit is {}".format(a))
	s=s+a
print("The sum of the digits of the entered integer is {}".format(s)) 