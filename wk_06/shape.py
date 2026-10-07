from abc import ABC, abstractmethod
import math

class Shape(ABC):

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if isinstance(val, str):
            self.__name = val
        else:
            raise TypeError

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):

    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


def add(x, y):
    return x + y

if __name__ == "__main__":
    r = Rectangle('Knuckle Joe',3,4)
    c = Circle('Waddle Dee', 3)
    print(add(1, 2))
    print(add([1, 2, 3], [4, 5, 6]))
    print(add('abc', 'xyz'))
    print(add(1.23, 4.56))