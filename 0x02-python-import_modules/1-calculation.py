#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, subtract, multiply, divide
    a = 10
    b = 5
    tsum = add(a, b)
    tdifference = subtract(a, b)
    tproduct = multiply(a, b)
    tquotient = divide(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, tsum))
    print("{:d} - {:d} = {:d}".format(a, b, tdifference))
    print("{:d} * {:d} = {:d}".format(a, b, tproduct))
    print("{:d} / {:d} = {:d}".format(a, b, tquotient))
