#!/usr/bin/python3
"""8-rectangle

This module provide ``Rectangle`` class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle.

    :param width: width of thr rectangle
    :type width: int
    :raise TypeError: width must be an integer
    :raise ValueError: width must be greater than 0
    :param height: height of the rectangle
    :type height: int
    :raise TypeError: height must be an integer
    :raise ValueError: height must be greater than 0
    """
    def __init__(self, width, height):
        """Initializer"""
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
