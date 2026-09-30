
class UnexpectedSide(Exception):
    pass

class Shape:

    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def perimeter(self):
        pass

    def circumference(self):
        pass

    def __str__(self):
        return f'{self.__class__.__name__}({self.name})'

class Rectangle(Shape):

    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length * 2) + (self.width * 2)

class Square(Rectangle):

    def __init__(self, name, side, width=0):
        if width == 0:
            super().__init__(name, side, side)
        elif width == side:
            super().__init__(name, side, width)
        else:
            raise UnexpectedSide('Square requires only one side')

if __name__ == "__main__":
    r = Rectangle('Jimmy the Rectangle', 3, 4)
    print(r.area())
    s = Square("Squarepants", 4)
    print(s.area())