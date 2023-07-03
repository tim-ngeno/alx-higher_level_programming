#!/usr/bin/python3
"""Divide values of a matrix"""


def matrix_divided(matrix, div):
    """Divides each value of a matrix by div
    Args:
        matrix: the list of elements to be divided
        div: the divisor
    Return:
        New matrix with elements divided
    """
    if not isinstance(matrix, (list)):
        raise TypeError("matrix must be a matrix (list of lists) of\
        integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        len_first_row = len(matrix[0])
        if len(row) != len_first_row:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError(
                    "matrix must be a matrix(list of lists) of integers/floats"
                )

            return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
