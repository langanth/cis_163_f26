def first_and_last(lst):
    return lst[0], lst[-1]

def total(lst):
    result = 0
    for x in lst:
        result += x
    return result

def count_halvings(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count

def has_duplicate(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False

def sort_and_find_median(lst):
    ordered = sorted(lst)       # Python's built-in sort (Timsort)
    return ordered[len(ordered) // 2]

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def multiply_matrices(A, B, n):
    # A and B are n x n matrices (lists of lists)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def doubling_inner_loop(lst):
    n = len(lst)
    count = 0
    for i in range(n):
        j = 1
        while j < n:
            count += 1
            j *= 2
    return count

def binary_search(lst, target, lo, hi):
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] < target:
        return binary_search(lst, target, mid + 1, hi)
    else:
        return binary_search(lst, target, lo, mid - 1)

def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

def countdown_with_work(n):
    if n <= 0:
        return
    for i in range(n):
        print(i)                 # O(n) work at each level
    countdown_with_work(n - 1)


def towers_of_hanoi(n, source, target, spare):
    if n == 0:
        return
    towers_of_hanoi(n - 1, source, spare, target)
    print(f"Move disk {n} from {source} to {target}")
    towers_of_hanoi(n - 1, spare, target, source)

def permutations(items):
    if len(items) <= 1:
        return [items[:]]
    result = []
    for i in range(len(items)):
        rest = items[:i] + items[i + 1:]       # O(n) to build
        for perm in permutations(rest):
            result.append([items[i]] + perm)   # O(n) to build
    return result