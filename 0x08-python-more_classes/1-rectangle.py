#!/usr/bin/python3
""" A Rectangle Module

This module provides a Class and methods to work with Rectangle.
"""


class Rectangle:
    """ Represents a `Rectangle`.
    """

    def __init__(self, width=0, height=0):
        """Initialize a `Rectangle` object.

        :param width: width of rectangle, defaults to 0
        :type width: int
        :param height: height of rectangle, defaults to 0
        :type height: int
        :raise TypeError: if `width` or `height` is not an integer
        :raise ValueError: if `width` or `height` <= 0
        :return: `Rectangle` object
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get Rectangle's Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set Rectangle's Width

        :param value: Rectangle width
        :type value: int
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

    @property
    def height(self):
        """Get Rectangle Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set Rectangle Height

        :param value: Rectangle height
        :type value: int
        """""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
