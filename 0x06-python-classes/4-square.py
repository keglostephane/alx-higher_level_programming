#!/usr/bin/python3
"""A square module

This module provides encapsulation to work with a square.
"""


class Square:
    """Defines a square.

    Attributes:
        size (int) : size of the square.
    """

    def __init__(self, size=0):
        """Square object initializer.

        Args:
                size (int, default=0) : size of the square.

        Returns:
                (Square) : a `Square` object.
        """
        self.__size = size

    def area(self):
        """Computes the square area.

        Returns:
                (int) :  area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Gets `size` attribute value.

        Returns:
                (int) : `size` value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets `size` attribute value.

        Args:
                value (int) : `size` attribute value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
