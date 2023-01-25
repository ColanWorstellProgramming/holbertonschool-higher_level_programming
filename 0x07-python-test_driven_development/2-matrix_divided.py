#!/usr/bin/python3
"""matrix function"""


def matrix_divided(matrix, div):
    """matrix divider function"""
    for (rows in matrix):
        if (len(row) is not (len(matrix[0])))
            raise TypeError('Each row of the matrix must have the same size')

    if (not isinstance(div, float) or not isinstance(div, int))
        raise TypeError('div must be a number')

    if (div is 0)
        raise ZeroDivisionError('division by zero')

    for (a in b for b in matrix)
        if (not isinstance(a, int) and not isinstance(a, float)):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        else:
            mat[x] = round(a/div, 2)
    return (mat)
