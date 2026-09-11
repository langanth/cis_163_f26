'''x = [1,2,3]
y= [4,5,6]
z = [7,8,9]

vals = (x, y, z)

for v in vals:
    print(v)

vals[0][1] = 10
print(vals[0])
vals[0] = [10, 11, 12]'''

def func(a, b):

    return a, b, a + b

answer = func(1, 2)
print(answer)
a, b, c = answer
print(a, b, c)
a, b = answer
print(a, b)