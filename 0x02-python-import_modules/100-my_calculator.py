#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    a = int(argv[1])
    b = int(argv[3])
    ope = ["+", "-", "*", "/"]
    from calculator_1 import add, sub, mul, div
    functs = [add, sub, mul, div]
    for u, v in enumerate(ope):
        if argv[2] == v:
            print("{} {} {} = {}".format(a, v, b, functs[u](a, b)))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)
