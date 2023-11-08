#!/usr/bin/python3
"""100-append_after

This module provide ``append_after`` that insert a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing
    a specific string.

    :param filename: name of source file, defaults to ""
    :type filename: str, optional
    :param search_string: string to search for in file, defaults to ""
    :type search_string: str, optional
    :param new_string: replacement string, defaults to ""
    :type new_string: str, optional
    """
    with open(filename, 'r+', encoding='utf-8') as fp:
        content = []
        while line := fp.readline():
            content.append(line)
            if search_string in line:
                content.append(new_string)
        fp.seek(0)
        fp.writelines(content)
