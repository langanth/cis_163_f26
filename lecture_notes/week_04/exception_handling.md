# Exceptions
- What happens when an error occurs?

# Exception Types
- Syntax Error: A problem with out syntax, occurs before runtime
	- sometimes a NameError occurs at this point as well
- Runtime Error: Gets raised if there is something wrong during python runtime
	- usually syntactically correct, but an impossible operation was called
- Logical Error: Syntactically and functionally correct, but the outcome is not the intended outcome
	- unexpected outcome
	- not designed for state

# Types of Errors - Common
- SyntaxError
- TypeError
- ValueError
- KeyError
- EOFError
- IndexError
- NameError
- ZeroDivisionError

# Exception Handling
- We can attempt to manage what happens when an error occurs
- This is through exception handling
- Try: attempts to run code
- Except: runs when the try block failse to execute without raising an error
- Else: runs only when the try block runs without error
- Finally: runs everytime