'''
Write a function that takes a list as the only argument and returns
(a) the number of odd items in the list;
(b) the average of all the items in the list;
(c) the sum of squared items in the list.
'''

def myFun1(x=[]):
    length=len(x)
    list1=[]
    for i in range(0,length):
        if(x[i]%2 != 0):
            list1.append(x[i])
    print("The odd numbers in the list: ")
    print(list1)
    print("The no. of odd numbers in the list: ")
    print(len(list1))
        


lst=[]
print("Question 1a")
n=int(input("Enter the no. of values in the array: "))
for i in range(0,n):
    ele = int(input("Enter the number: "))
    lst.append(ele)
myFun1(lst)


def myFunc2(x=[]):
    a=0
    s=0
    length=len(x)
    for i in range(0,length):
        s=s+x[i]
    
    a=float(s/length)
    print("The sum of all the elemnents in the array is {}".format(s))
    print("The average of all the elements in the array is {}".format(a))
    

lst=[]
print("\nQuestion 1b")
n=int(input("Enter the number of elements for the array: "))
for i in range(0,n):
    ele=int(input("Enter the number: "))
    lst.append(ele)
myFunc2(lst)


def myFunc3(x=[]):
    square=0
    s=0
    length=len(x)
    for i in range(0,length):
        import math
        square= pow(x[i],2)
        s=s+square
    print("The sum of square of all the numbers in the array is {}.".format(s))
    

lst=[]
print("\nQuestion 1c")
n=int(input("Enter the no. of elements in the array: "))
for i in range(0,n):
    ele=int(input("Enter the numbers: "))
    lst.append(ele)
myFunc3(lst)



