#!/usr/bin/python3
def uppercase(str):
    for upp in str:
        if ord('a') <= ord(upp) <= ord('z'):
            upp = chr(ord(upp) - 32)
            print(upp, end='')
