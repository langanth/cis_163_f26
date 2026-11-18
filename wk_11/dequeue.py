from collections import deque

d = deque(['a', 'b', 'c'])

print(d)
print(d[0])
d.append('d')
d.appendleft('e')
print(d)
d.rotate(1)
print(d)
d.rotate(-2)
print(d)
print(d.popleft())
print(d.pop())
print(d)