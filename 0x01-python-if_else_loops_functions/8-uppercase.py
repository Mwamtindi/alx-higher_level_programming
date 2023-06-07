#!/usr/bin/python3
def uppercase(str):
    for upp in str:
        if ord(upp) >= 97 and ord(upp) <= 122:
            upp = chr(ord(upp) - 32)
            print("{:s}".format(upp), end='')
            print('\n', end="")
