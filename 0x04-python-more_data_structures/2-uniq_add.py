#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list.

    :param my_list: list of integers, defaults to []
    :type my_list: list, optional
    :return: the sum of unique integers in the list.
    :rtype: int
    """
    if my_list is not None:
        return sum(set(my_list))
