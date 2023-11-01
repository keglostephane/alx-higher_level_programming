#!/usr/bin/python3
"""5-text_indentation

This module provides the ``text_indentation`` function that prints a text
with 2 new lines after some specific characters.
"""


def text_indentation(text):
    """Print a text with 2 new lines after each of these characters:
    ``.``, ``?``, ``:``.

    :param text: a string
    :type text: str
    :raises TypeError: text must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for char in text:
        print("{}".format(char), end="")
        if char in ('.', '?', ':'):
            print("\n")
