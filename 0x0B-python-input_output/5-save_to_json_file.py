#!/usr/bin/python3
"""5-save_to_json_file

This module provide ``save_to_json_file`` that writes an object to a text file,
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation.

    :param my_obj: the object to serialize
    :type my_obj: any
    :param filename: name of the text file
    :type filename: str
    """
    with open(filename, 'r+', encoding='utf-8') as fp:
        json.dump(my_obj, fp)
