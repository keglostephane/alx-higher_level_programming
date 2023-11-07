#!/usr/bin/python3
"""101-add_attribute

This module try to adds a new attribute to an object if it is possible.
Otherwise, raise a TypeError exception
"""


def add_attribute(obj, name, value):
    """Try to add a new attribute to an existing object.

    :param obj: obj to add attribute to
    :type obj: any
    :param name: name of the new attribute
    :type name: str
    :param value: value of the new attribute
    :type value: any
    :raise TypeError: can't add new attribute
    """
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
