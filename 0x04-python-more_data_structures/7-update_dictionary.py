#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary.

    Args:
    a_dictionary (dict) :  a dictionary
    key (string) : a dictionary key to access values
    value (any) :  a value in the dictionary

    Returns:
    (dict) : an updated dictionary with value at `key` updated
    with `value`.

    if a key exists in the dictionary, the value will be replaced.
    if a key doesn't exist in the dictionary, it will be created.
    """
    if key not in a_dictionary:
        a_dictionary.setdefault(key, value)
    else:
        a_dictionary[key] = value
    return a_dictionary
