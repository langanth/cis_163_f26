from abc import ABC, abstractmethod

class Fun(ABC):

    def __init__(self, name):
        pass

    @abstractmethod
    def method_one(self):
        pass
    
    def method_two(self):
        pass

class SuperFun(Fun):

    def __init__(self, name, other_thing):
        super().__init__(name)
        self.other_thing = other_thing

    def method_one(self):
        # code go brrrr
        pass