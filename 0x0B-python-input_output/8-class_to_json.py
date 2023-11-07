#!/usr/bin/python3
"""8-class_to_json

This module provide ``class_to_json`` that returns the dictionary description
for JSON serialization of an aobject.
"""


def class_to_json(obj):
    """Return the dictionary description with simple data structure
       of an object for JSON serialization.

    :param obj: an instance of class
    :type obj: any
    :return: dictionary description of an object
    :rtype: dict
    """
    return obj.__dict__
