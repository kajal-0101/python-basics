'''
Write a function that takes a list of numbers as the only argument and returns a
list of numbers that contains all the multiples of 3 in the argument;
'''

def myFunc(x=[]):
    list1=[]
    length=len(x)
    for i in range(0,length):
        if(x[i]%3 == 0):
            list1.append(x[i])
    print("The list of elements which are multiple of 3 are: {}".format(list1))

lst=[]
n=int(input("Enter the number of elements for the array: "))
for i in range(0,n):
    ele=int(input("Enter the number: "))
    lst.append(ele)
print("The entered list of elements {}".format(lst))
myFunc(lst)
