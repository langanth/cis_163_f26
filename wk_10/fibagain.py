from time import time

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n - 2)

def fibm(n, cache=None):
    if cache is None:
        cache = {}

    if n in cache:
        return cache[n]

    if n <= 1:
        return n

    result = fibm(n - 1, cache) + fibm(n - 2, cache)
    cache[n] = result
    return result

def fibt(n):
    if n <= 1:
        return n
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


if __name__ == "__main__":
    n = 450000
    print('Starting non-memoized fib')
    start = time()
    print(fib(n))
    print(time()-start)
    print('='*25)
    print('Starting memoized fib')
    start = time()
    print(fibm(n))
    print(time() - start)
