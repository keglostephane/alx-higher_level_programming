#!/usr/bin/python3
"""A module that allow to work with rectangle.
"""


class Rectangle:
    """Define a rectangle.

    :param width: width of the rectangle, defaults to 0
    :type with: int, optional
    :raises TypeError: width must be an integer
    :raises ValueError: width must be >= 0
    :param height: height of the rectangle, defaults to 0
    :type height: int, optional
    :raises TypeError: height must be an integer
    :raises ValueError: height must be >= 0
    """
    def __init__(self, width=0, height=0):
        """Initialize a rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle.

        :return: the actual size of the rectangle.
        :rtype: int
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        :param value: value of the rectangle
        :type value: int
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.

        :return: the actual height of the rectangle
        :rtype: int
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        :param value: the height of the rectangle
        :type value: int
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
