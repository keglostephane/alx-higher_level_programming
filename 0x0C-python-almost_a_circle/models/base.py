#!/usr/bin/python3
"""A Base class module
"""


class Base:
    """A base class.

    :param id: id of a ``Base`` instance
    :type id: int
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation.

        :param list_dictionaries: a list of dictionaries
        :type list_dictionaries: list
        :return: JSON string representation of list of dictionaries
        :rtype: str
        """
        import json

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
