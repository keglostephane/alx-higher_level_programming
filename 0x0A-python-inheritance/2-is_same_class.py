#!/usr/bin/python3
"""2-is_same_class

This module provide ``is_same_class that checks if an object is exactly an
instance of a specified class.
"""


def is_same_class(obj, a_class):
    """Return True if the object is exactly an instance of the specified
       class.

    :param obj: the object to check
    :type obj: any
    :param a_class: the class the object must be an instance
    :type a_class: any
    :return: True if ``obj`` is an exact instance of ``a_class``,
             otherwise False
    :rtype: bool
    """
    return type(obj) is a_class
