
def make_sandwhich(bread: str, protein: str, cheese: str) -> int:
    print(f'{protein} with w/{cheese} on {bread}')
    return 3

def better_sandwhich(bread: str, protein: str, cheese: str, *args) -> None:
    print(f'{protein} with w/{cheese} on {bread}')
    if args:
        for i in args:
            print(f'\t{i}')

def even_better_sandwhich(bread: str, protein: str, cheese: str, **kwargs: int|float) -> None:
    print(f'{protein} with w/{cheese} on {bread}')
    if kwargs:
        for k, a in kwargs.items():
            print(f'\t{k}: {a}')

# even_better_sandwhich('bread', 'protein', 'cheese')

if __name__ == "__main__":
    make_sandwhich('sourdough', 'ham', 'provolone')
    better_sandwhich('sourdough', 'ham', 'provolone', 'mustard', 'pickles', 'ketchup', 'onions', 'au jus', 'raw egg')
    even_better_sandwhich('sourdough', 'ham', 'provolone', condiment1='mayo', condiment2='mustard', topping1='pickles')
    print('Apple', 'Banana', sep=" & ", end=' ')
    print('and potatoes')