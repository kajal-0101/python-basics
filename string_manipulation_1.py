# python to program to delete a character from the string if it is follwed by a '#' symbol.

a = input("Enter the string: ")
print("Input String: ",a)


li = []
temp = []

for i in a:
	li.append(i)


for i in li:
	if (i!="#"):
		temp.append(i)
	else:
		if(len(temp) != 0):
			temp.pop()

st = ''

for i in temp:
	st += i

if(st == ''):
	print("Output String: ''")
else:
	print("Output String: ", st)
