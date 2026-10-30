"""
Write a function called fibonnaci that takes an integer
and returns its value in the fibonacci sequence

i.e. fibonacci(7) -> 0, 1, 1, 2, 3, 5, 8, 13 -> 13
"""
import time

def fibonacci(num):
    if num <= 2:
        return 1

    last, bl = 1, 0
    for i in range(num-1):
        fib = last + bl
        bl = last
        last = fib
    return fib

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n - 2)

if __name__ == "__main__":
    x = 40
    print('Non Recursive')
    start = time.time()
    print(fibonacci(x))
    print(time.time() - start)
    print('Recursive')
    start = time.time()
    print(fib(x))
    print(time.time() - start)