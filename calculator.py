"""
Square     : w**2
Rectangle  : w*h
Triangle   : 1/2*w*h
Circle     : Pi*r**2
"""


class Rectangle():
    name = "Rectangle instance with area : "

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def __str__(self) -> str:
        return self.name + str(self.width * self.height)


if __name__ == '__main__':
    # Rectangle.name = "xxx"
    r1 = Rectangle(25, 15)
    print(r1)
    print("My rectangle area is : " + str(r1.area()))
