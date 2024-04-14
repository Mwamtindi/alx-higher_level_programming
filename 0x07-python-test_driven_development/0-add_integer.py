#!/usr/bin/python3

"""integers addition in unittest"""


def add_integer(a, b=98):
    """Result of integer addition of a and b.

    Perform check to know if a and b are ints before addition
    Raises:
    TypeError: if one of them is non-integer or float
    OverflowError: if the addition result exceeds the maximum integer value
    ValueError: if one of the values is a float NaN
    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or float")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer or float")

    try:
        return int(a) + int(b)
    except OverflowError:
        raise OverflowError("integer addition large to convert to int")
    except ValueError:
        raise ValueError("cannot convert float NaN to integer")
