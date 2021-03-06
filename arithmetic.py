def add(num1, num2):
    """Return the sum of two numbers"""
    return num1 + num2

def subtract(num1, num2):
    """Return the difference of two numbers"""
    return num1 - num2

def multiply(num1, num2):
    """Return the product of two numbers"""
    return num1 * num2

def divide(num1, num2):
    """Return the quotient of two numbers as a float"""
    return float(num1 / num2)

def square(num):
    """Return the square of a number"""
    return num**2

def cube(num):
    """Return the cube of a number"""
    return num**3

def power(num, exponent):
    """Return num raised to the power of exponent"""
    return num**exponent

def mod(num1, num2):
    """Return remainder of num1 divided by num2"""
    return num1 % num2

print add(2, 3)
print subtract(10, 89)
print multiply(10, 3)
print divide(2000, 1000)
print square(63)
print cube(2567)
print power(2, 3)
print mod(10, 3)