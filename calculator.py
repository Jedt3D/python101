"""
Square     : w**2
Rectangle  : w*h
Triangle   : 1/2*w*h
Circle     : Pi*r**2
"""
from Area.Rectangle import Rectangle
from Area.Triangle import Triangle

if __name__ == '__main__':
    # Rectangle.name = "xxx"
    r1 = Rectangle(25, 15)
    print(r1)
    print("My rectangle area is : " + str(r1.area()))

    t1 = Triangle(15, 7)
    print(t1)
    print("My triangle area is : " + str(t1.area()))
