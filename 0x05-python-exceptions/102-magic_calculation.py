#!/usr/bin/python3
def magic_calculation(a, b):
    res = 0
    for w in range(1, 3):
        try:
            if w > a:
                raise Exception('Too far')

            res += a ** b / w
        except:
            res = b + a
            break
        return res
