# math_operations.py

# The provided code stub reads two integers from USER INPUT, a and b. Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.


def calculate_operations(a, b):
    sum = a+b
    diff = a-b
    prod = a*b
    return sum, diff, prod

a = float(input("Enter first number:\t"))
b = float(input("Enter Second number:\t"))

print(calculate_operations(a,b))
