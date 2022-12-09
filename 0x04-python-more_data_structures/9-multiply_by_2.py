#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2.

    Args:
    a_dictionary (dict) : a dictionary

    Returns:
    (dict) : a new dictionary with all values multiplied by 2.
    """
    return {key: value * 2 for (key, value) in
            zip(a_dictionary.keys(), a_dictionary.values())}
