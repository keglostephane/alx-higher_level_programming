#!/usr/bin/python3
"""0-read_file

This module provide ``read_file`` that reads a text file and print it
to stdout.
"""


def read_file(filename=""):
    """Read a file and print its content to stdout.

    :param filename: name of the file to print
    :type filename: str
    """
    with open(filename, encoding="utf-8") as fp:
        for line in fp.readlines():
            print(line, end="")
