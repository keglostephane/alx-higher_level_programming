#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix.

    Args:
    matrix (list) : list of integers

    Returns:
    (list) : a new matrix list with sme size as the original.

    Each value in the matrix list should be the square of the
    value of the input.

    Examples:
    >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> new_matrix = square_matrix_simple(matrix)
    >>> print(new_matrix)
    [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
    >>> print(matrix)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    if matrix == []:
        return []
    else:
        new_matrix = [[num ** 2 for num in row] for row in matrix]
        return new_matrix
