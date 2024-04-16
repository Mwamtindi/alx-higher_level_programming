#!/usr/bin/python3
"""A module that defines pascal_triangle function."""


def pascal_triangle(n):
    """
    Generate the Pascal's triangle up to n rows.

    Args:
    - n: The number of rows in the triangle.

    Returns:
    - list of lists of int:Pascal's triangle as a list of lists.
    """
    if n <= 0:
        return []

    tri = [[1]]

    for e in range(1, n):
        pr = tri[e - 1]
        new_row = [1] + [pr[g] + pr[g + 1] for g in range(len(pr) - 1)] + [1]
        tri.append(new_row)

    return tri
