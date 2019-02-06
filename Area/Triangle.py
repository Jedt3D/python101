from Area.Shape import Shape


class Triangle(Shape):
    name = "Triangle instance with area : "

    def area(self):
        return 1 / 2 * self.width * self.height

    def __str__(self) -> str:
        return self.name + str(1 / 2 * self.width * self.height)