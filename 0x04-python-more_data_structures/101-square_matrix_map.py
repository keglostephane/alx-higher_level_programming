#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """Computes the square value of all integers of a matrix

    Args:
    matrix (list) : a two dimensional list of integers

    Returns:
    (list) : a two dimensional list which contains square value of
    of all integers of `matrix`.
    """
    return list(map(lambda l: list(map(lambda x: x ** 2, l)), matrix))
