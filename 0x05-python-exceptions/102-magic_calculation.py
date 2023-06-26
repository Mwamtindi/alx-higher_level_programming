#!/usr/bin/python3


def magic_calculation(a, b):
    res = 0

    for s in range(1, 3):
        try:
            if s > a:
                raise Exception('Too far')

            res += a ** b / s
        except:
            res = b + a
            break

    return res
