#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        tsum = add(a, b)
        for e in range(4, 6):
            tsum = add(tsum, e)
        return tsum
    else:
        return (sub(a, b))
