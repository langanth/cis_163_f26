# How do we know if our code works?
- seriously, how do we know?

# How do we test our code?
- Print statements
- random data
- post ypur code on reddit/stackoverflow to get annihilated
- Ask chatgpt/claude

# Test Driven Development
- Tests are written before their corresponding functions - [IBM](https://www.ibm.com/think/topics/test-driven-development)
- The Cycle
	- Write unit test
	- write code
	- run test
	- rewrite code to pass test
	- repeat

# Unit Testing in Python
- Unittest
	- built-in
- Pytest
	- external library

# Unittest
- standard built-in
- class based
- assertions are methods using self
- verbose

# Pytest
- third-party package
- functions are bare assert
- fixtures injected as arguments

# So... which one?
- Depends
	- Team
	- Dependency allowance