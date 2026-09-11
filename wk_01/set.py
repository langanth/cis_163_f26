s = set()
s = {1, 2, 3}

s.add(4)
print(s)
s.add(1)
print(s)

for i in s:
    print(i)

alpha1 = {'a','b','c'}
alpha2 = {'c','d','e'}

print(alpha1.difference(alpha2))
print(alpha2.difference(alpha1))
print()
print(alpha1.intersection(alpha2))
print()
# returns whether two sets have a intersection or not
print(alpha1.isdisjoint(alpha2))

for i in range(3):
    print(s.pop())
print(s)
s.remove(4)
print(s)

lst = [i for i in range(10)]
x = lst.pop()
print(x)
print(lst)