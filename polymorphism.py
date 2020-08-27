'''
Write a python program to find the surface area and volume of below given shapes
using polymorphism. 
'''
'''
Formulae:
Sphere:
SA = 4(pi)r^2
V = 4/3(pi)r^3

Cylinder:
SA = 2(pi)r^2 + 2(pi)rh
V = (pi)r^2h

Cone:
SA = (pi)rs + (pi)r^2
V = (1/3)(pi)r^2h

Rectangular Prism:
SA = 2(lw + lh + wh)
V = lwh

Triangular Prism:
SA = bh + 2ls + lb
V = (1/2)(bl)h
'''
import math
class Sphere:
    def __init__(self, radius):
        self.__radius = radius
    
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = radius
        
    def get_sa(self):
        return math.pi * 4 * self.__radius ** 2
    
    def get_v(self):
        return (4/3) * math.pi * self.__radius ** 3

class Cylinder:
    def __init__(self, rad, height):
        self.__rad = rad
        self.__height = height
        
    def get_rad(self):
        return self.__rad

    def get_height(self):
        return self.__height
    
    def set_rad(self, rad):
        self.__rad = rad
        
    def set_height(self, height):
        self.__height = height;
        
    def get_sa(self):
        return ((2 * math.pi * self.__rad ** 2) + (2 * math.pi *self.__rad * self.__height))
    
    def get_v(self):
        return math.pi * self.__height * self.__rad ** 2

class RectPrism:
    def __init__(self, length, width, height):
        self.__length = length
        self.__width = width
        self.__height = height

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def set_length(self):
        self.__length = length

    def set_height(self):
        self.__height = height

    def set_width(self):
        self.__width = width
    
    def get_sa(self):
        return (2 * (self.__length * self.__width) * (self.__length * self.__height) * (self.__width * self.__height))

    def get_v(self):
        return ((self.__length) * (self.__width) * (self.__height))

class TriPrism:
    def __init__(self, length, breadth, surface, height):
        self.__length = length
        self.__breadth = breadth
        self.__surface = surface
        self.__height = height

    def get_length(self):
        return self.__length

    def get_breadth(self):
        return self.__breadth

    def get_surface(self):
        return self.__surface

    def get_height(self):
        return self.__height

    def set_length(self):
        self.__length = length

    def set_height(self):
        self.__height = height

    def set_breadth(self):
        self.__breadth = breadth

    def set_surface(self):
        self.__surface = surface
    
    def get_sa(self):
        return ((self.__breadth * self.__height) * (2 * self.__length * self.__surface) * (self.__length * self.__breadth))

    def get_v(self):
        return ((1/2) * (self.__breadth * self.__length) * self.__height)

class Cone:
    def __init__(self, rad, surface, height):
        self.__rad = rad
        self.__surface = surface
        self.__height = height

    def get_rad(self):
        return self.__rad

    def get_surface(self):
        return self.__surface

    def get_height(self):
        return self.__height

    def set_rad(self):
        self.__rad = rad

    def set_height(self):
        self.__height = height

    def set_surface(self):
        self.__surface = surface
    
    def get_sa(self):
        return ((math.pi * self.__rad * self.__surface) * (math.pi * self.__rad ** 2))

    def get_v(self):
        return ((1/3) * (math.pi * (self.__rad** 2) * self.__height)) 

print("\nSphere")
r_sphere = int(input("Enter the radius: "))
sphere = Sphere(r_sphere)
print("Radius of the sphere is {}".format(sphere.get_radius()))
print("Surface area of the sphere is {}".format(sphere.get_sa()))
print("Volume of the sphere is {}".format(sphere.get_v()))

print("\nCylinder")
r_cylinder = int(input("Enter the radius: "))
h_cylinder = int(input("Enter the height: "))
cylinder = Cylinder(r_cylinder, h_cylinder)
print("Radius of the cylider is {} and height of the cylinder is {}".format(cylinder.get_rad(), cylinder.get_height()))
print("Surface area of the cylinder is {}".format(cylinder.get_sa()))
print("Volume of the cylinder is {}".format(cylinder.get_v()))

print("\nCone")
r_cone = int(input("Enter the radius: "))
s_cone = int(input("Enter the surface: "))
h_cone = int(input("Enter the height: "))
cone = Cone(r_cone, s_cone, h_cone)
print("Radius of the cone is {}, height of the cone is {} and surface of the cone is {}".format(cone.get_rad(), cone.get_height(), cone.get_surface()))
print("Surface area of the cone is {}".format(cone.get_sa()))
print("Volume of the cone is {}".format(cone.get_v()))

print("\nTraingular Prism")
l_tp = int(input("Enter the radius: "))
b_tp = int(input("Enter the breadth: "))
h_tp = int(input("Enter the height: "))
s_tp = int(input("Enter the surface: "))
tri_prism = TriPrism(l_tp, b_tp, s_tp, h_tp)
print("Length of the Traingular Prism is {}, breadth of the Traingular Prism is {}, surface of the Traingular Prism is {} and height of the Traungular Prism is {}".format(tri_prism.get_length(), tri_prism.get_breadth(), tri_prism.get_surface(), tri_prism.get_height()))
print("Surface area of the rectangular prism is {}".format(tri_prism.get_sa()))
print("Volume of the rectangular prism is {}".format(tri_prism.get_v()))

print("\nRectangular Prism")
l_rp = int(input("Enter the length: "))
w_rp = int(input("Enter the width: "))
h_rp = int(input("Enter the height: "))
rect_prism = RectPrism(l_rp, w_rp, h_rp)
print("Length of the Rectangular Prism is {}, width of the Rectangular Prism is {} and height of the Rectangular Prism is {}".format(rect_prism.get_length(), rect_prism.get_width(), rect_prism.get_height()))
print("Surface area of the rectangular prism is {}".format(rect_prism.get_sa()))
print("Volume of the rectangular prism is {}".format(rect_prism.get_v()))
