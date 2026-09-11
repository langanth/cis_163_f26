from func import even_better_sandwhich
from random import randint

class Dog:

    def __init__(self, name: str, breed: str, legs: int=4, tail: bool=True) -> None:
        self.name = name
        self.breed = breed
        self.legs = legs
        self.tail = tail

    def bark(self) -> None:
        print(f'{self.name} goes bork bork!')

    def bark_at(self, target):
        print(f'{self.name} goes bork bork at {target.name}!')

    def get_legs(self) -> int:
        return self.legs

    def set_legs(self, num_legs) -> None:
        if num_legs > self.legs:
            return
        self.legs = num_legs

    def hit_by_car(self) -> None:
        ceiling = self.get_legs()
        self.set_legs(randint(0, ceiling))
        if randint(0, 1) == 0:
            self.tail = False
        print(f'Oh no, {self.name} got hit by a car. It currently has {self.get_legs()} legs.')

if __name__ == "__main__":
    zeke = Dog('Zeke', 'Shih-Tzu')
    zeke.bark()
    dug = Dog('Dug', 'Labrador Retreiever')
    zeke.bark_at(dug)
    print(zeke.get_legs())
    zeke.set_legs(3)
    zeke.legs = 4
    print(zeke.get_legs())
    zeke.hit_by_car()
    while zeke.legs > 0:
        zeke.hit_by_car()