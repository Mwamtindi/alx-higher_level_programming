#!/usr/bin/python3

"""integers addition in unittest"""


def add_integer(a, b=98):
    """Add two integers or floats and return the result as an integer.

    Args:
        a (int, float): The first number.
        b (int, float): The second number.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.
        OverflowError: If the result of the addition exceeds the maximum integer value.
        ValueError: If either `a` or `b` is a float NaN.

    Returns:
        int: The result of the addition.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or float")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer or float")

    try:
        return int(a) + int(b)
    except OverflowError:
        raise OverflowError("integer addition result is too large to convert to int")
    except ValueError:
        raise ValueError("cannot convert float NaN to integer")

