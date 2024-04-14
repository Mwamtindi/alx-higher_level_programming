#!/usr/bin/python3
"""matrix_divided - divides a specified matrix by div(division) number"""


def matrix_divided(matrix, div):
    """
    Args:
        Each row of the matrix must be of the same size
        matrix must be a list of lists of integers or floats
        div must be a number (integer or float)
        div can’t be equal to 0

    Raises:
        TypeError:
            matrix must be a matrix (list of lists) of integers/floats
            Each row of the matrix must have the same size
            div must be a number
        ZeroDivisionError:
            division by zero

    Returns: a new matrix rounded to 2 decimal places
    """

    result_matrix = []

    output = "matrix must be a matrix (list of lists) of integers/floats"
    output1 = "Each row of the matrix must have the same size"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError(output1)

        in_matrix = []
        for nenos in lists:
            if not isinstance(nenos, (int, float)):
                raise TypeError(output)
            else:
                in_matrix.append(round(nenos / div, 2))
        result_matrix.append(in_matrix)

    return result_matrix
