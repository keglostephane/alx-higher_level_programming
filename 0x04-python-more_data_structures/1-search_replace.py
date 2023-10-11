#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurences of an element by another in a new list.

    :param my_list: the initial list
    :type my_list: list
    :param search: the element to replace in the list
    :type search: int
    :param replace: the new element
    :type replace: int
    :return: a new list with all occurences of `search` replaced by `replace`
    :rtype: list
    """
    if my_list is not None:
        return [replace if elem is search else elem for elem in my_list]
