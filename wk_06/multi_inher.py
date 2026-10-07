
class A:

    def __init__(self):
        self.a = 'A'

class B:

    def __init__(self):
        self.b = 'B'

class C(A, B):

    def __init__(self):
        # super().__init__()
        A.__init__(self)
        B.__init__(self)
        self.c = 'C'

if __name__ == "__main__":
    c = C()
    print(c.c, c.a, c.b)

