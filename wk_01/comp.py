from random import randint, seed
seed(42)

lst = [i for i in range(10)]
nums = [randint(1,100) for _ in range(10)]
print(nums)

lst = [i for i in range(10) if i % 2 == 0]
print(lst)


ob[j]