#!/usr/bin/python3
"""append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing
    a specific string.

    :param filename: name of source file
    :type filename: str
    :param search_string: string to search for in file
    :type search_string: str
    :param new_string: replacement string
    :type new_string: str
    """
    with open(filename, 'a+', encoding='utf-8') as f:
        while line := f.readline():
            if search_string in line:
                f.write(new_string)
