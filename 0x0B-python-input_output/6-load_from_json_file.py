#!/usr/bin/python3
"""6-load_from_json_file

This module provide ``load_from_json_file`` that create an object from a
JSON file.
"""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file.

    :param filename: name of the JSON file
    :type filename: str
    :return: the decoded object
    :rtype: any
    """
    with open(filename, encoding='utf-8') as fp:
        return json.load(fp)
