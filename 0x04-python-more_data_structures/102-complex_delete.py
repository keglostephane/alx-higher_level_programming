#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Delete keys with a specific value in a dictionary.

    :param a_dictionary: a dictionary
    :type a_dictionary: dict
    :param value: value and associated key to delete if exists
    :type value: any
    :return: the dictionary with value and keys deleted if found.
        If the value doesn't exist, the dictionary won't change.
        All keys having the searched value have to be deleted.
    """
    if a_dictionary is not None:
        value_keys = [key for key in a_dictionary.keys()
                      if a_dictionary[key] == value]
        for key in value_keys:
            del a_dictionary[key]
        return a_dictionary
