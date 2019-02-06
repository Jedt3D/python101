class Shape:
    def __init__(self, w, h):
        self.height = h
        self.width = w

    def area(self):
        return self.width * self.height