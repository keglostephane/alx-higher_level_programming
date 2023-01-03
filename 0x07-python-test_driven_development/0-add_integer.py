#!/usr/bin/python3
"""add_integer Module

This module allows to perform addition on integers.
"""


def add_integer(a, b=98):
    """Adds two integers.

    :param a: First operand
    :type a: int, float, optional
    :param b: Second operand
    :type b: int, float, defaults to `98`
    :raises TypeError: ``a must be an integer`` or ``b must be an integer``
    :return: The addition of `a` and `b`
    :rtype: int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif isinstance(a, float):
        a = int(a)

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    elif isinstance(b, float):
        b = int(b)

    return a + b
