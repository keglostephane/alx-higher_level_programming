#!/usr/bin/python3
"""10-square

This module provide a ``Square`` class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square.

    :param size: size of the square
    :type size: int
    :raise TypeError: size must be an integer
    :raise valueError: size must be greater than 0
    """
    def __init__(self, size):
        """Initializer"""
        self.__size = super().integer_validator("size", size)

    def area(self):
        """Compute the area of the square.

        :return: the area of the square
        :rtype: int
        """
        return self.__size ** 2

    def __str__(self):
        """Human readable represantation of Square"""
        return Rectangle(self.__size, self.__size).__str__()
