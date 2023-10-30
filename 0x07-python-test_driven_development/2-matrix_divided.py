#!/usr/bin/python3
"""2-matrix_divided

this module provides the matrix_divided function that divide all elemnts
of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    :param matrix: list of list of integers or floats
    :type matrix: list
    :raises TypeError: matrix must be a matrix(list of lists) of
                       integers/floats
    :raises TypeError: Each row of the matrix must have the same size
    :param div: number that divides matrix's elements
    :type div: int, float
    raises TypeError: `div` must be a number
    raises ZeroDivisionError: division by zero
    :return: a new matrix
    :rtype: list
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        size = len(matrix[0])

        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")

        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not div:
        raise ZeroDivisionError("division by zero")

    return [[float("{:.2f}".format(num / div)) for num in row]
            for row in matrix]
