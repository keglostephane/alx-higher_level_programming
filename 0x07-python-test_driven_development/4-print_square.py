#!/usr/bin/python3
"""4-print_square

This module provide ``print_square`` that prints a square with the character #
"""


def print_square(size):
    """Print a square with the character #.

    :param size: size of the square
    :type size: int
    :raises TypeError: size must be an integer
    :raises ValueError: size must be >= 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
