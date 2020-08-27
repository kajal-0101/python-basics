'''
The sum of all odd numbers between 0 and 100 that make sin(x) > 0 (using math module)
'''

import math
print("This program will find the sum of all the odd numbers between 0 to 100 which make sin(x) > 0")
s=0
for i in range(1,101):
	if(i%2!=0):
		if(math.sin(i)>0):
			s=s+i
print("The sum is {}".format(s))