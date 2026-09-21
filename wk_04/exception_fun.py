
try:
    num1 = int(input('Enter an integer: '))
    num2 = int(input('Enter another integer: '))

    print(num1 / num2)

except ZeroDivisionError:
    print('You cannot divide by zero!')

except Exception as e:
    print(e)
    print(type(e))
    print('You entered an invalid value')
    raise ValueError

else:
    print('You successfully divided two values!')


finally:
    print('Now closing program!')