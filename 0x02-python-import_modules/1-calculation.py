# imports from the file calculator_1.py
from calculator_1 import add, subtract, multiply, divide

# define variables
a = 10
b = 5

# compute the result with imported functions
result = add(a, b)
result = subtract(result, b)
result = multiply(result, a)
result = divide(result, b)

# print the result
print(f'result is {result}')
