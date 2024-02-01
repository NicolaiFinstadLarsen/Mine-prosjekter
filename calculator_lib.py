#https://www.matematica.pt/en/useful/math-formulas.php

from math import pi
from fractions import Fraction

class nico:

  class area:

    def Square(lengt_of_sides):
      l = lengt_of_sides
      print("Area of this square is:")
      print(l**2)
    
    def Rectangle(width, height):
      w = width
      h = height
      print("Area of this Rectangle is:")
      print(w*h)

    def Triangle(base, height):
      b = base
      h = height
      print("Area of this Triangle is:")
      print((b*h)/2)

    def Rhombus(large_diagonal, small_diagonal):
      L = large_diagonal
      l = small_diagonal
      print((L*l)/2)

    def Trapezoid(large_side, small_side, height):
      l = large_side
      s = small_side
      h = height
      print("Area of this Trapezoid is:")
      print(((l+s)/2)*h)

  class volumes:

    def cube(s):
      print("Volum of this cube is:")
      print(s**3)
    
    def Parallelepiped(length, width, height):
      l = length
      w = width
      h = height
      print("Volum of Parallelepiped is: ")
      print(l*w*h)

    def Regular_prism(base, height):
      b = base
      h = height
      print("Volume of this regular prism is:")
      print(b*h)

    def Cylinder(radius, height):
      r = radius
      h = height
      print("Volum for this cylinder is:")
      print((pi*r**2)*h)

    def Cone(base, height):
      b = base
      h = height
      #f= Fraction(1,3)
      print("Volume for this cone or pyramid is:")
      print(((0.333333333*b)*h))

    def sphere(radius):
      r = radius
      print("Volume of this sphere is:")
      print(1.3333333333*pi*(r**3))
  
#nico.area.Trapezoid(10,7,3)
