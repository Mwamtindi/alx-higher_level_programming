#!/usr/bin/pytthon3

"""integers addition in unittest"""

def add_integer(a, b=98):
    """Result of integer addition of a and b.

    Perform check to know if a and b are ints before addition
    Raises:
    TypeError: if one of them is non-integer or float
    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integger")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
