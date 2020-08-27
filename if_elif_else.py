'''
Area of circle, triangle and rectangle
'''

r=input("Enter the value of r: ")
b=input("Enter the value of b: ")
h=input("Enter the value of h: ")
print("1)Find the area of the circle")
print("2)Find the area of the triangle")
print("3)Find the diagonal of the rectangle")
val=input("choose among the following : ")
val=int(val)
#print("The selected choice is")
#print(val)
if val == 1:
    print("Option 1 has been selected")
    import math
    radius=float(r)
    pi=3.14
    areac=pi*pow(radius,2)
    print("The area of the circle is:")
    print(areac)
elif val == 2:
    print("Option 2 has been selected")
    import math
    base=float(b)
    height=float(h)
    areat=0.5*base*height
    print("The area of the triangle is:")
    print(areat)
elif val == 3:
    print("Option 3 has been selected")
    import math
    b=int(b)
    h=int(h)
    base2=pow(b,2)
    height2=pow(h,2)
    add=base2+height2
    result=math.sqrt(add)
    print("Diagonal of the triangle is")
    print(result)
else:
    print("No option selected")
