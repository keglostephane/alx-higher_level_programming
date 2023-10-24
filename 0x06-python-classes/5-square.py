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

        self.__size = size

    @property
    def size(self):
        """Get the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        :param value: new value of the square
        :type value: int
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return square area.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#'.
        """
        if not self.__size:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
