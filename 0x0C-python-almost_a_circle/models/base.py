#!/usr/bin/python3
"""A Base class module
"""


class Base:
    """A base class.

    :param id:
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
