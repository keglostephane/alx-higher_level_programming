#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary

    Args:
    a_dictionary (dict) : a dictionary
    key (str) : a dictionary key

    Returns:
    (dict) : updated dictionary with `key` deleted.

    if a key doesn't exist, the dictionary won't change.
    """
    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary
