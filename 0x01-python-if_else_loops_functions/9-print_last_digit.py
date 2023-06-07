#!/usr/bin/python3
def print_last_digit(number):
    '''prints the last digit of a number'''
    dlast = abs(number) % 10
    print(f"{dlast}", end='')
    return dlast
