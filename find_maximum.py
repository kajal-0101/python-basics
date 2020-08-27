'''
Repeatedly asks the user to enter an integer, until the user enter 0, after which
the maximum of all the numbers is shown
'''

print("The array will take value until 0 is entered")
li=[]
count=0
while True:
	ele=int(input("\nEnter the value for the array: "))
	if(ele==0):
		print("Entering value is over\n")
		break
	li.append(ele)
	count=count+1
	print("\nThe entered elements are")
	print("The entered element is {}".format(li))
print("Total number of elements are: {}".format(count))
m=0
for i in range(0,count):
	if(m<li[i]):
		m=li[i]
print("The maximum value of the array is {}".format(m))