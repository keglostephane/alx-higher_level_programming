#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary.

    :param a_dictionary: a dictionary
    :type a_dictionary: dict
    :param key: an existing/missing key in the dictionary, defaults to ""
    :type key: str, optional
    :return: the dictionary with the existing key/value deleted.
        if the key doesn't exist, the dictionary won't change
    :rtype: dict
    """
    if a_dictionary is not None:
        if key in a_dictionary.keys():
            del a_dictionary[key]
        return a_dictionary
