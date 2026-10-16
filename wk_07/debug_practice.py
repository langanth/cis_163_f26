"""
DEBUGGING PRACTICE
==================
This file contains 1 instructor demo plus 7 exercises (4 functions and 3 classes).
Each one has a bug.
Your job is NOT to guess the fix by staring at the code.
Use a debugger to watch what the program actually does, then find the bug.

HOW TO RUN
----------
  python debugging_practice.py            # just run it and see what fails
  python -m pdb debugging_practice.py     # start in the command-line debugger
  (or use the debugger in VS Code/ set breakpoints)

You can also add this line anywhere to pause execution there:
  breakpoint()

PDB CHEAT SHEET
---------------
  n          next line (steps OVER function calls)
  s          step INTO a function or method call
  c          continue until next breakpoint
  r          run until the current function returns
  p expr     print an expression, e.g.  p total
  pp expr    pretty-print, e.g.  pp counts
  p self.__dict__   show all attributes of an object
  l          list source code around the current line
  w          show the call stack (where am I?)
  u / d      move up / down the call stack
  b 25       set a breakpoint on line 25
  b 25, i==2 set a breakpoint that only triggers when i == 2
  q          quit

FOR EACH EXERCISE
-----------------
  1. Run the file and see which check fails.
  2. Set a breakpoint inside the function or method.
  3. Step through line by line, printing variables as you go.
  4. Write down: which line is wrong, and why?
  5. Fix it and re-run until you see [PASS].
"""


# ===========================================================================
# DEMO: LIVE WALKTHROUGH (instructor-led)
# ===========================================================================
# Use this one to show the whole debugger workflow before students start.
# It has a helper function (to show `n` vs `s`), a loop (to show variables
# changing), and a bug that only affects SOME of the data.
#
# Goal: calculate the total amount due across a list of invoices, including
# late fees:
#   - more than 30 days late: 5% fee
#   - more than 7 days late:  2% fee
#   - otherwise:              no fee
#
# Suggested demo path:
#   1. Put `breakpoint()` (or a breakpoint at the `for` line) in total_due().
#   2. Use `n` to step over the loop body, printing `total` and `fee`.
#   3. On the third invoice, use `s` to step INTO late_fee().
#   4. Print `days_late`, then step line by line and ask: which branch ran?
# ---------------------------------------------------------------------------
def late_fee(amount, days_late):
    if days_late > 7:
        percent = 2
    elif days_late > 30:
        percent = 5
    else:
        percent = 0
    return amount * percent / 100


def total_due(invoices):
    total = 0
    for invoice in invoices:
        fee = late_fee(invoice["amount"], invoice["days_late"])
        total += invoice["amount"] + fee
    return total


# ===========================================================================
# PART A: FUNCTIONS
# ===========================================================================

# ---------------------------------------------------------------------------
# Exercise 1: The Missing Number
# Goal: return the average of a list of numbers.
# Try watching: the variables `i` and `total` on each pass through the loop.
# ---------------------------------------------------------------------------
def average(numbers):
    total = 0
    for i in range(1, len(numbers)):
        total += numbers[i]
    return total / len(numbers)


# ---------------------------------------------------------------------------
# Exercise 2: The Stubborn Zero
# Goal: return the largest number in a list.
# Try watching: the variable `largest` before the loop starts.
# ---------------------------------------------------------------------------
def find_largest(numbers):
    largest = 0
    for n in numbers:
        if n > largest:
            largest = n
    return largest


# ---------------------------------------------------------------------------
# Exercise 3: The Sort That Works (Sometimes)
# Goal: sort a list from smallest to largest using bubble sort.
# Notice that the first test passes but the second fails. Why?
# Try watching: `i`, `j`, and `items` after every swap.
# ---------------------------------------------------------------------------
def bubble_sort(items):
    items = list(items)
    n = len(items)
    for i in range(n - 1):
        for j in range(n - 2 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items


# ---------------------------------------------------------------------------
# Exercise 4: The Word Counter
# Goal: count how many times each word appears in a sentence.
# Try watching: the dictionary `counts` and the current `word`.
# Use `pp counts` to see it clearly.
# ---------------------------------------------------------------------------
def word_counts(text):
    counts = {}
    for word in text.lower().split():
        counts[word] += 1
    return counts


# ===========================================================================
# PART B: CLASSES
# ===========================================================================

# ---------------------------------------------------------------------------
# Exercise 5: The Shared Ledger
# Goal: every BankAccount should keep its OWN list of transactions.
# Try watching: after creating two accounts, run
#   p a.transactions is b.transactions
#   p a.__dict__
#   p BankAccount.__dict__
# Where does `transactions` actually live?
# ---------------------------------------------------------------------------
class BankAccount:
    transactions = []

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("deposit", amount))

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(("withdraw", amount))


# ---------------------------------------------------------------------------
# Exercise 6: The Discount That Keeps Discounting
# Goal: total(discount_percent) should return the discounted total
# WITHOUT changing the prices stored in the cart. Calling it twice with
# the same discount should give the same answer both times.
# Try watching: `self.items` before and after each call to total().
# ---------------------------------------------------------------------------
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, name, price):
        self.items.append({"name": name, "price": price})

    def apply_discount(self, percent):
        for item in self.items:
            item["price"] = item["price"] * (1 - percent / 100)

    def total(self, discount_percent=0):
        if discount_percent:
            self.apply_discount(discount_percent)
        return sum(item["price"] for item in self.items)


# ---------------------------------------------------------------------------
# Exercise 7: The Missing Parent
# Goal: an HonorsStudent is a Student who also has a mentor.
# Try watching: step INTO the constructor with `s`, then run
#   p self.__dict__
# at the end of __init__. Which attributes exist? Which are missing?
# ---------------------------------------------------------------------------
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades)


class HonorsStudent(Student):
    def __init__(self, name, mentor):
        self.mentor = mentor

    def describe(self):
        return f"{self.name} (mentor: {self.mentor})"


# ===========================================================================
# TEST RUNNER (you don't need to change anything below this line)
# ===========================================================================
def check(label, func, args, expected):
    try:
        result = func(*args)
    except Exception as e:
        print(f"[ERROR] {label}: {type(e).__name__}: {str(e)[:60]}")
        return
    status = "PASS" if result == expected else "FAIL"
    print(f"[{status}] {label}: expected {expected!r}, got {result!r}")


def account_demo():
    a = BankAccount("Ana")
    b = BankAccount("Ben")
    a.deposit(100)
    b.deposit(50)
    return len(a.transactions)


def cart_demo():
    cart = ShoppingCart()
    cart.add("Book", 20.0)
    cart.add("Pen", 10.0)
    cart.total(10)  # first call
    return round(cart.total(10), 2)  # second call should match the first


def invoice_demo():
    invoices = [
        {"amount": 100, "days_late": 0},
        {"amount": 200, "days_late": 10},
        {"amount": 300, "days_late": 45},
    ]
    return total_due(invoices)


def honors_demo():
    student = HonorsStudent("Zoe", "Dr. Lee")
    return student.describe()


def main():
    print("Running checks...\n")
    check("DEMO. total_due() with late fees", invoice_demo, (), 619)
    check("1. average([10, 20, 30, 40])", average, ([10, 20, 30, 40],), 25.0)
    check("2. find_largest([-5, -2, -9])", find_largest, ([-5, -2, -9],), -2)
    check("3a. bubble_sort([5, 1, 4, 2, 8])", bubble_sort, ([5, 1, 4, 2, 8],), [1, 2, 4, 5, 8])
    check("3b. bubble_sort([4, 3, 2, 1])", bubble_sort, ([4, 3, 2, 1],), [1, 2, 3, 4])
    check("4. word_counts('the cat and the hat')", word_counts,
          ("the cat and the hat",), {"the": 2, "cat": 1, "and": 1, "hat": 1})
    check("5. Ana's transaction count", account_demo, (), 1)
    check("6. cart total(10) called twice", cart_demo, (), 27.0)
    check("7. HonorsStudent.describe()", honors_demo, (), "Zoe (mentor: Dr. Lee)")


if __name__ == "__main__":
    main()