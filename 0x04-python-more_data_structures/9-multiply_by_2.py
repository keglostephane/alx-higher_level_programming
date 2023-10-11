#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multiplied by 2

    :param a_dictionary: a dictionary
    :type a_dictionary: dict
    :return: a new dictionary with all values multiplied by 2
    :rtype: dict
    """
    if a_dictionary is not None:
        return {key: value * 2 for key, value in a_dictionary.items()}
