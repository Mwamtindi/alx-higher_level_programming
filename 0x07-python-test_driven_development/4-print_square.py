#!/usr/bin/python3
"""Function that prints a square with character #"""


def print_square(size):
    """Prints a square  using the character '#'."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if size == 0:
        return

    for _ in range(size):
        print('#' * size)
