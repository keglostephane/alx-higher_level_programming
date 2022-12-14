#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary.

    Args:
    a_dictionary (dict)
    value (any) : value to search in the dictionary

    Returns:
    (dict) : a dictionary with all keys having the searched value deleted.

    If the value doesn't exist, returns the original dictionary.
    """
    keys_to_delete = [key for key in a_dictionary.keys()
                      if a_dictionary[key] == value]
    for key in keys_to_delete:
        del a_dictionary[key]
    return a_dictionary
