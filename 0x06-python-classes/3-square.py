#!/usr/bin/python3
"""A module that allows to work with squares.
"""


class Square:
    """Represents a square.
    """
    def __init__(self, size=0):
        """Initialize a square.

        :param size: size of the square, defaults to 0
        :type size: int, optional
        :return: a Square object with a size of `size`
        :rtype: Square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return square area.
        """
        return self.__size ** 2
