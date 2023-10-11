#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key:value in a dictionary.

    :param a_dictionary: a dictionary
    :type a_dictionary: dict
    :param key: an existing key or new key to add to the dictionnary
    :type key: str
    :param value: an existing value or new value to add to the dictionary
    :type value: any
    :return: the dictionary with the new key/value pair added.
        if a key exists, the value will be replaced.
        if a key doesn't exist it will be created
    :rtype: dict
    """
    if a_dictionary is not None:
        if key in a_dictionary.keys():
            a_dictionary[key] = value
        else:
            a_dictionary.update({key: value})
    return a_dictionary
