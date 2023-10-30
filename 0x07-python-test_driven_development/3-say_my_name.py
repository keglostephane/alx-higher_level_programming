#!/usr/bin/python3
"""3-say_my_name

This module provides ``say_my_name`` function that prints
<first name><last name>
"""


def say_my_name(first_name, last_name=""):
    """Print My name is <first name><last name>

    :param first_name: first name
    :type first_name: str
    :raises TypeError: first_name must be a string
    :param last_name: last name, defaults to ""
    :type last_name: str, optional
    :raises TypeError: last_name must be a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
