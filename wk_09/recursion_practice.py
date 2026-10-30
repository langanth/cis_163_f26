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
    pass


"""
Using recursion, determine if two lists are
identical with one another

comp_list([1,2,3], [1,2,3]) -> True
comp_list([3,2,1], [1,2,3]) -> False
"""

def comp_list(lsta, lstb):
    pass

"""
Given a list, determine of whether or not it
if it can be split where both sides of a list
have the same total sum

balance([1, 2, 3]) -> True
balance([2, 2, 3]) -> False
balance([10, 1, 2, 3, 4]) -> True

"""

def balance():
    pass


"""
Given two lists, weave them together, alternating values
"""

def weave(a, b):
    pass
