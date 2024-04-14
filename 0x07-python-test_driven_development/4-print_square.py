#!/usr/bin/python3
"""Function that prints a square with character #"""


def print_square(size):
    """
    size: size must be an integer, if not raise a
        TypeError exception with the message size must be an integer

    If size < 0:
        ValueError: size must be >= 0
    If size is a float, raise a
        TypeError exception with the message size must be an integer
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for t in range(size):
        print("#" * size)
