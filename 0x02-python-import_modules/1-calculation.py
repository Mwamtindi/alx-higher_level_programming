#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    tsum = add(a, b)
    tdifference = sub(a, b)
    tproduct = mul(a, b)
    tquotient = div(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, tsum))
    print("{:d} - {:d} = {:d}".format(a, b, tdifference))
    print("{:d} * {:d} = {:d}".format(a, b, tproduct))
    print("{:d} / {:d} = {:d}".format(a, b, tquotient))
