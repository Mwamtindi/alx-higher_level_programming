#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, subtract, multiply, divide
    a = 10
    b = 5
    tsum = add(a, b)
    tdifference = subtract(a, b)
    tproduct = multiply(a, b)
    tquotient = divide(a, b)
    print(f"{a} + {b} = {tsum}")
    print(f"{a} - {b} = {tdifference}")
    print(f"{a} * {b} = {tproduct}")
    print(f"{a} / {b} = {tquotient}")
