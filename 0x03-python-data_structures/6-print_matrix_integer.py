#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        x = '\n'.join([' '.join(['{}'.format(x) for x in row])])
        print(x)
