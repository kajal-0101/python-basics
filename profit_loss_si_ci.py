'''
Program to calculate the profit, loss, simple interest and compund interest
'''

import math
loss = lambda sp, cp: 0 if sp>cp else cp - sp
print("\nLambda function to check incurred loss")
m = int(input("Enter Cost Price: "))
n = int(input("Enter Selling Price: "))
l = loss(n, m)
print("The selling price is Rs. {} and the cost price is Rs. {}".format(n,m))
print("The incurred loss is {}".format(l))

profit = lambda sp, cp: 0 if cp>sp else sp - cp
print("\nLambda function to check gained profit")
q = int(input("Enter Cost Price: "))
e = int(input("Enter Selling Price: "))
k = profit(e, q)
print("The selling price is Rs. {} and the cost price is Rs. {}".format(e,q))
print("The incurred profit is {}".format(k))

si = lambda p, r, t: 0 if p<0 or r<0 or t<0 else (p*r*t)/100
print("\nLambda function to calculate Simple Interest")
p = int(input("Enter the principal amount: "))
r = int(input("Enter the rate per annum: "))
t = int(input("Enter the no. of years: "))
j= si(p,r,t)
print("The principal amoount is {}, the rate per annum is {} and the no. of years is {}".format(p,r,t))
print("The SI on the principal amount is {}".format(j))

ci = lambda p,i,t: 0 if p<0 or i<0 or t<0 else p*math.pow((1+i/100),t) -p
print("\nLambda function to calculate Compound Interest")
p1=int(input("Enter the principal amount: "))
i=int(input("Enter the compound rate of interest: "))
t1=int(input("Enter the time period: "))
v=ci(p1,i,t1)
print("The principal amoount is {}, the compound rate of interest is {} and the no. of years is {}".format(p1,i,t1))
print("The CI on the principal amount is {}".format(v))