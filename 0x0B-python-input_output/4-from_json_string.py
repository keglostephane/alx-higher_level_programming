#!/usr/bin/python3
"""4-from_json_string

This module provide ``from_json_string`` that returns an object represented
by a JSON string
"""
import json


def from_json_string(my_str):
    """Return an Python object represented by a JSON string.

    :param my_str: a JSON string
    :type my_str: str
    :return: the Python object represented by the JSON string
    :rtype: any
    """
    return json.loads(my_str)
