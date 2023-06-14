#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for nrow in matrix:
        nnew_row = []
        for nnum in nrow:
            nnew_row.append(nnum ** 2)
        new_matrix.append(nnew_row)
    return new_matrix
