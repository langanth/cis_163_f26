
class Canine:

    def __init__(self, name):
        self.name = name

    def make_noise(self):
        print(f'{self.name} goes,', end=' ')

    def __cant_do_this(self):
        print('hahahahahaahahahaha')

    def __str__(self):

        return f'{self.__class__.__name__}({self.name})'

class Wolf(Canine):

    def make_noise(self):
        super().make_noise()
        print('awwwwooooo')


class Dog(Canine):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_noise(self):
        # super().__cant_do_this()
        super().make_noise()
        print('bork bork!')

    def __str__(self):
        st = super().__str__()[:-1]
        return st + f', {self.breed})'

if __name__ == "__main__":
    c = Canine('Doglike thing')
    w = Wolf('Wolfy')
    d = Dog('Dug', 'Beagle')

    c.make_noise()
    print()
    w.make_noise()
    d.make_noise()
    print(c)
    print(w)
    print(d)
