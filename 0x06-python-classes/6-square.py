#!/usr/bin/python3
"""A square module

This module provides abstraction to work with a square.
"""


class Square:
    """Defines a square.

    Instance Attributes:
        size (int) : size of the square.
        position (tuple) : position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Square object initializer.

        Args:
                size (int, default=0) : size of the square.
                position(tuple, default=(0,0): position of the square.

        Returns:
                (Square) : a `Square` object.
        """
        self.size = size
        self.position = position

    def area(self):
        """Computes the square area.

        Returns:
                (int) :  area of the square
        """
        return self.size ** 2

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

    @property
    def position(self):
        """Gets `position` attribute value.

        Returns:
                (tuple) : `position` value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets `position` attribute value.

        Args:
                value (tuple) : `position attribute value`
        """
        error = "position must be a tuple of 2 positive integers"

        if type(value) is not tuple:
            raise TypeError(error)
        elif type(value) is tuple and (len(value) < 2 or len(value) > 2):
            raise ValueError(error)
        elif type(value) is tuple and (type(value[0]) is not int or
                                       value[0] < 0):
            raise ValueError(error)
        elif type(value) is tuple and (type(value[1]) is not int or
                                       value[1] < 0):
            raise ValueError(error)
        else:
            self.__position = value

    def my_print(self):
        """Prints the square with the character `#`"""
        offset_x = self.position[0]
        offset_y = self.position[1]
        offset_char = ' '
        side = self.size
        if side == 0:
            print("")
        else:
            for y in range(offset_y):
                print("")
            for i in range(side):
                for x in range(offset_x):
                    print(offset_char, end='')
                for j in range(side):
                    print("#", end='')
                print("")

    def __str__(self):
        """human-readable representation of Square object"""
        if self.size == 0:
            return ""
        else:
            return '\n' * self.position[1] + \
                (' ' * self.position[0] + '#' * self.size + '\n') * \
                (self.size - 1) + ' ' * self.position[0] + '#' * self.size
