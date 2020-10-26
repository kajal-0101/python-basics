# python program to check whether the given two strings are anagram or not

a = input("Enter the first word: ")
b = input("Enter the second word: ")

print("1st Word: ", a)
print("2nd Word: ", b)


if (len(a) != len(b)):
	print("Anagram is not possible")
else:
	li_1 = []
	li_2 = []
	flag = 0
	for i in a:
		li_1.append(i)
	for i in b:
		li_2.append(i)
	li_1.sort()
	li_2.sort()
	if (li_1 == li_2):
		print("The words are anagram")
	else:
		print("The words are not anagram")