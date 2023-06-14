#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None or len(matrix) == 0:
        return None
    matrix_copy = matrix.copy()
    y = [[x**2 for x in row] for row in matrix_copy]
    return y
