from Area.Shape import Shape


class Rectangle(Shape):
    name = "Rectangle instance with area : "

    def __str__(self) -> str:
        return self.name + str(self.width * self.height)