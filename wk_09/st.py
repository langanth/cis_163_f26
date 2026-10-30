
def func(st):
    if len(st) <= 0:
        return ''
    return func(st[1:]) + st[0]

if __name__ == "__main__":
    st = 'abc'
    for i in st:
        print(i, end='')
    print()

    print(func(st))
    print((1, 2) + (2))
