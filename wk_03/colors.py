
class Color:

    def __init__(self, red=0, green=0, blue=0):
        self.red = red
        self.green = green
        self.blue = blue

    def check_valid(self, value):
        if isinstance(value, int):
            if 0 <= value <= 255:
                return value
            else:
                raise ValueError('Value is not between 0-255')
        else:
            raise TypeError('Value must be an integer!')
            
    @property
    def red(self):
        return self.__red

    @red.setter
    def red(self, value):
        self.__red = self.check_valid(value)