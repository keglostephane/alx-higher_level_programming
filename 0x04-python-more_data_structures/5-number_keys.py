#!/usr/bin/python3
def number_keys(a_dictionary):
    """Returns the number of keys in a dictionary.

    Args:
    a_dictionary (dict) : a dictionary

    Returns:
    (int) : number of keys in `a_dictionary`

    Examples:
    >>> a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
    >>> nb_keys = number_keys(a_dictionary)
    >>> print("Number of keys: {:d}".format(nb_keys))
    Number of keys: 3
    """
    if a_dictionary == {}:
        return 0
    else:
        return len(a_dictionary.keys())
