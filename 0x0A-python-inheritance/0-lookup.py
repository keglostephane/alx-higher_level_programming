#!/usr/bin/python3
"""0-lookup

This module provide ``lookup`` function that lists all available attrinutes
and methods of an object.
"""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    :param obj: any python object
    :type obj: list
    :return: a list of all available attributes and methods of ``object``
    :rtype: list
    """
    return dir(obj)
