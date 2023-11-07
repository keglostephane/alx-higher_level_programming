#!/usr/bin/python3
"""7-base_geometry

This module provide ``BaseGeometry`` class.
"""


class BaseGeometry:
    """An Base Geometry class.
    """
    def area(self):
        """Not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a value.

        :param name: name of the value
        :type name: str
        :param value: value of ``name``
        :type value: int
        :raise TypeError: <name> must be an integer
        :raise ValueError: <name> must be greater than 0
        :return: the value of ``value``
        :rtype: int
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

        return value
