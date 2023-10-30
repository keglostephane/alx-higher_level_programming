#!/usr/bin/python3
"""0-add_integer

This module provides the ``add_integer`` function that retuns the sum of two
integers.
"""


def add_integer(a, b=98):
    """Add two integers.

    :param a: first integer
    :type a: int, float
    :param b: second integer, defaults to 98
    :type b: int, float, optional
    :raises TypeError: if `a` and `b` are integers or floats
    :return: the addition of `a` and `b`
    :rtype: int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
