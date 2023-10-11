#!/usr/bin/python3
def number_keys(a_dictionary):
    """Returns the number of keys in a dictionary.

    :param a_dictionary: a dictionary
    :type a_dictionary: dict
    :return: the numbers of keys in the dictionary
    :rtype: int
    """
    if a_dictionary is not None:
        return len(a_dictionary.keys())
