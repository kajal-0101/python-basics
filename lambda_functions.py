'''
Write a python program using lambda function The Head Librarian at a library wants you to make a program that calculates the fine for returning the book after the return date. 
You are given the actual and the expected return dates. Calculate the fine as follows:
a. If the book is returned on or before the expected return date, no fine will be charged, in other words fine is 0.
b. If the book is returned in the same month as the expected return date, Fine = 15 Rupees × Number of late days
c. If the book is not returned in the same month but in the same year as the expected return date, Fine = 50 Rupees × Number of late months
d. If the book is not returned in the same year, the fine is fixed at 1000 Rupees.
'''

print("This program calculates fine")
print("Enter due date")
d1=int(input("Enter the day: "))
m1=int(input("Enter the month: "))
y1=int(input("Enter the year: "))
print("Enter return date")
d2=int(input("Enter the day: "))
m2=int(input("Enter the month: "))
y2=int(input("Enter the year: "))
if(y1==y2 or y1>y2):
	if(m1==m2):
		if(d1==d2):
			a4=lambda a: a
			b4=a4(0)
			print("The fine incurred is Rs.{}".format(b4))
		else:
			a3=lambda a: a*abs(d2-d1)
			b3=a3(15)
			print("The fine incurred is Rs.{}".format(b3))
	else:
		a2=lambda a: a * abs(m2-m1)
		b2=a2(50)
		print("The fine incurred is Rs.{}".format(b2))
else:
	a1=lambda a: a
	b1=a1(1000)
	print("The fine incurred is Rs.{}".format(b1))