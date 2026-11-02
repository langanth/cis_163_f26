"""
Take a string and return a new
string without the vowels
using recursion

disemvowel('abc') -> 'bc'
"""

def disemvowel(st):
    #Base case: No more string
    if len(st) == 0:
        return ''

    #Recursive Case: when there is string if vowel, don't add
    if st[0].lower() in 'aeiou':
        return '' + disemvowel(st[1:])

    #Recursive Case: when therei s string, but cosonant, add
    else:
        return st[0] + disemvowel(st[1:])

"""
Given a stair case of x amount of steps, determine
how many different ways you can climb up
the stairs based on either choosing to go
up the stairs one or two stairs at a time

stair_case(1) -> 1
stair_case(2) -> 2
stair_case(4) -> 5
"""

def stair_case(steps):
    if steps == 0 or steps == 1:
        return 1
    return stair_case(steps - 1) + stair_case(steps - 2)


"""
Given an integer, add all values counting
down until a stopping point.

i.e. add_range(5, 2) -> 5 + 4 + 3 -> 12
"""

def add_range(start, stop):
    
    # Base Case
    if start == stop:
        return 0

    # Recursive Case
    return start + add_range(start - 1, stop)

"""
Given an integer, add up the values
that make it up.

sum_digits(78) -> 15
sum_digits(11) -> 2
sum_digits(100011100011101) -> 8

Extra challenge: No strings
"""

def sum_digits(num):
    # Base
    if num == 0:
        return 0
    # Recursive
    return (num % 10) + sum_digits(num // 10)


"""
Using recursion, determine if two lists are
identical with one another

comp_list([1,2,3], [1,2,3]) -> True
comp_list([3,2,1], [1,2,3]) -> False
"""

def comp_list(lsta, lstb):

    # Base Case 1
    if len(lsta) != len(lstb):
        return False

    # Base Case 2
    if len(lsta) == 0 and len(lstb) == 0:
        return True

    if lsta[0] == lstb[0]:
        return comp_list(lsta[1:], lstb[1:])
    return False

"""
Given a list, determine of whether or not it
if it can be split where both sides of a list
have the same total sum

balance([1, 2, 3]) -> True
balance([2, 2, 3]) -> False
balance([10, 1, 2, 3, 4]) -> True

"""

def balance(lst, idx=1):
    # Base Case
    if idx >= len(lst):
        return False
    
    # Base Case 2
    if  sum(lst[:idx]) == sum(lst[idx:]):
        return True

    # Recursive Case
    return balance(lst, idx + 1)


"""
Given two lists, weave them together, alternating values
lists do not have to be of equal length
"""

def weave(a, b):
    pass

if __name__ == "__main__":
    print(balance([10,1,2,3,4]))
    print([1]+[2])