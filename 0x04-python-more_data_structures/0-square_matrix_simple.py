#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix.

    :param matrix: a 2 dimensional array, defaults to []
    :type matrix: list
    :return: a new matriw with the same size as `matrix`.
        Each value should be the square of the value of the input
    :rtype: list
    """
    if matrix is not None:
        return [[elem ** 2 for elem in row] for row in matrix]
