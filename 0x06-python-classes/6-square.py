#!/usr/bin/python3
"""A module that allows to work with squares.
"""


class Square:
    """Represents a square.

    :param size: size of the square, defaults to 0
    :type size: int, optional
    :param position: coordinates of the square, defaults to 0
    :type position: tuple, optional
    :return: a Square object with a size of `size`
    :rtype: Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Get the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.
        """
        error = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TypeError(error)
        if len(value) != 2:
            raise TypeError(error)
        if type(value[0]) is not int:
            raise TypeError(error)
        if value[0] < 0:
            raise TypeError(error)
        if type(value[1]) is not int:
            raise TypeError(error)
        if value[1] < 0:
            raise TypeError(error)

        self.__position = value

    def area(self):
        """Return square area.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#'.
        """
        if not self.__size:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for j in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
