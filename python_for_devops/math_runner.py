from functions import *

def main():
    print("Math Functions Demo")
    print("===================")
    
    # Test basic operations
    a, b = 10, 5
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    print(f"{a} / {b} = {divide(a, b)}")
    print(f"{a} % {b} = {modulus(a, b)}")
    print(f"{a} ^ {b} = {power(a, b)}")
    
    # Test other functions
    print(f"abs(-7) = {absolute(-7)}")
    print(f"min({a}, {b}) = {minimum(a, b)}")
    print(f"max({a}, {b}) = {maximum(a, b)}")
    print(f"round(3.14159, 2) = {round_number(3.14159, 2)}")
    print(f"floor(3.7) = {floor(3.7)}")
    print(f"ceiling(3.2) = {ceiling(3.2)}")

if __name__ == "__main__":
    main()