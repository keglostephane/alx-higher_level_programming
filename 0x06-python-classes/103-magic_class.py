#!/usr/bin/python3
"""This module provides:
MagicClass: Defines a circle.
Attributes:
        radius: radius of the circle
Methods:
        area: computes the area of the circle
        circumference: computes the circumference of the circle
"""
import math


class MagicClass:
    """Define a circle.

    :param radius: radius of the circle
    :type radius: int, float
    """
    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """Return the area of the circle.

        :return: circle's area
        :rtype: int, float
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the circle.

        :return: circle's circumference
        :rtype: int, float
        """
        return self.__radius * 2 * math.pi
