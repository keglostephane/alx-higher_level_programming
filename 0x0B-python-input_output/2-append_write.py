#!/usr/bin/python3
"""2-append_write

This module provide ``append_write`` that append a string at the end of
a text file.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file.

    :param filename: name of the file, defaults to ""
    :type filename: str, optional
    :param text: string to append, defaults to ""
    :type text: str, optional
    :return: the number of characters written
    :rtype: int
    """
    with open(filename, 'a', encoding='utf-8') as fp:
        written = fp.write(text)
    return written
