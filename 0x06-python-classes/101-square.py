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
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square.

        :return: the actual size of the square
        :rtype: int
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        :param value: new value of the square
        :type value: int
        :raises TypeError: if size is not an integer
        :raises ValueError: if size is negative
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Get the position of the square.

        :return: the actual position of the square
        :rtype: tuple
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        :param value: new value of the position
        :type value: tuple
        :raises TypError: if value is not a tuple of 2 positive integers
        """
        error = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TypeError(error)
        if len(value) != 2:
            raise TypeError(error)
        if type(value[0]) is not int or value[0] < 0:
            raise TypeError(error)
        if type(value[1]) is not int or value[1] < 0:
            raise TypeError(error)

        self.__position = value

    def area(self):
        """Return square area.

        :return: the area of the square
        :rtype: int
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
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        """Human readable representation of the square.
        """
        if not self.__size:
            return ""
        else:
            str1 = "\n" * self.__position[1]
            str2 = (" " * self.__position[0] + "#" * self.__size + '\n') * \
                (self.__size - 1)
            str3 = " " * self.__position[0] + "#" * self.__size

            return str1 + str2 + str3
