def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def modulus(x, y):
    return x % y

def power(base, exponent):
    return base ** exponent

def absolute(x):
    return abs(x)

def minimum(x, y):
    return min(x, y)

def maximum(x, y):
    return max(x, y)

def round_number(x, decimals=0):
    return round(x, decimals)

def floor(x):
    import math
    return math.floor(x)

def ceiling(x):
    import math
    return math.ceil(x)