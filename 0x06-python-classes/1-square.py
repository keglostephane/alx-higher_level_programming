#!/usr/bin/python3
"""A module that allows to work with squares.
"""


class Square:
    """Represents a square.

    :param size: size of the square
    :type size: int
    """
    def __init__(self, size):
        """Initialize a square.
        """
        self.__size = size
