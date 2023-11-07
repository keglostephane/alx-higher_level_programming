#!/usr/bin/python3
"""3-to_json_string

This module provides ``to_json_string`` function  that returns the
JSON representation of an object.
"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object.

    :param my_obj: the object
    :type my_obj: any
    :return: the JSON representation of the object
    :rtype: str
    """
    return json.dumps(my_obj)
