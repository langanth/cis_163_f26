class T:
    t_calls = 0

    def call(cls):
        T.t_calls += 1
        print('calling T')

class L(T):
    l_calls = 0
    
    def call(cls):
        super().call()
        print('calling L')
        L.l_calls += 1
    
class R(T):
    r_calls = 0

    def call(cls):
        super().call()
        print('calling R')
        R.r_calls += 1

class B(L, R):
    b_calls = 0

    def call(cls):
        L.call(cls)
        R.call(cls)
        print('calling B')
        B.b_calls += 1

if __name__ == "__main__":
    b = B()
    b.call()
    print(b.b_calls, b.l_calls, b.r_calls, b.t_calls)
    print(B.b_calls)

    words = ''.join(['a','b','c'])
    print(str(words))