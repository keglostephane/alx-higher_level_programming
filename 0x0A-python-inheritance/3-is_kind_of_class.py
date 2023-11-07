#!/usr/bin/python3
"""3-is_kind_of_class

This module provide ``is_kind_of_class`` that checks if an object is an
instance of, or if the object is an instance of a class that inherited from
a specified class.
"""


def is_kind_of_class(obj, a_class):
    """Return True if the object is an instance of, or the object is
       an instance of class that inherited from the specified class.

    :param obj: the object to check
    :type obj: any
    :param a_class: the class, the object must be an instance of, or
                    the class of the object must inherit from
    :type a_class: any
    :return: True if ``obj`` is an instance of ``a_class``, or
             if  the class of ``obj`` is an instance of ``a_class``,
             otherwise False
    :rtype: bool
    """
    return isinstance(obj, a_class)
