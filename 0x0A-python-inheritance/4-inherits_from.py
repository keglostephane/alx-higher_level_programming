#!/usr/bin/python3
"""4-inherits_from

This module provide ``inherits_from`` that checks if an object is an instance
of a class that inherited (directly of indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """Return True if the object is an instance of the class that inherited
       (directly or indirectly) from the a specified class.

    :param obj: object to check
    :type obj: any
    :param a_class: the class, the object's class must inherit from
    :return: True if ``obj`` is an instance of class that inherited
             from ``a_class``, otherwise False
    :rtype: bool
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
