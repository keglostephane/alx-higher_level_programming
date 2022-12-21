#!/usr/bin/python3
"""A square module

This module provides encapsulation to work with a square.
"""


class Square:
    """Defines a square.

    Attributes:
        size (int) : size of the square
    """

    def __init__(self, size):
        """Square object initializer
        """
        self.__size = size
