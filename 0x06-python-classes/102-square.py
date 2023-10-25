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

    def __eq__(self, square):
        """Return True if square objects have the same area.

        :param square: another square object
        :type square: Square
        :return: True if they have the same area, else False
        :rtype: bool
        """
        return True if self.area() == square.area() else False

    def __ne__(self, square):
        """Return True if square objects area are differents.

        :param square: another square object
        :type square: Square
        :return: True if they have different area, otherwise False
        :rtype: bool
        """
        return True if self.area() != square.area() else False

    def __le__(self, square):
        """Return True if area of the first square is less than or equal
        to the area of the second square.

        :param square: another square object
        :type square: Square
        :return: True if area of the first square is less than or equal to
                 the area of the second square, otherwise False
        :rtype: bool
        """
        return True if self.area() <= square.area() else False

    def __lt__(self, square):
        """Return True if the area of the first square is less than
        the area of the second square.

        :param square: another square object
        :type square: Square
        :return: True if area of the first square is less than
                 the area of the second square, otherwise False
        :rtype: bool
        """
        return True if self.area() < square.area() else False

    def __ge__(self, square):
        """Return True if the area of the first square is greater than or equal
        to the area of the second square.

        :param square: another square object
        :type square: Square
        :return: True if area of the first square is greater than or equal to
                 the area of the second square, otherwise False
        :rtype: bool
        """
        return True if self.area() >= square.area() else False

    def __gt__(self, square):
        """Return True if the area of the first square is greater than
        the area of the second square.

        :param square: another square object
        :type square: Square
        :return: True if area of the first square is greater than
                 the area of the second square, otherwise False
        :rtype: bool
        """
        return True if self.area() > square.area() else False
