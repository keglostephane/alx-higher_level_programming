#!/usr/bin/python3
"""1-write_file

This provide ``write_file`` that writes a string to a text file.
"""


def write_file(filename="", text=""):
    """Write a string to a text file.

    :param filename: name of the file
    :type filename: str
    :param text: string to write to the file
    :type text: str
    :return: the number of characters written
    :rtype: int
    """
    with open(filename, 'w', encoding='utf-8') as fp:
        written = fp.write(text)
    return written
