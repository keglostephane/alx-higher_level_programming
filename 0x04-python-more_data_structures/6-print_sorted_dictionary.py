#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys.

    Args:
    a_dictionary (dict) : a dictionary

    Returns:
    None

    Examples:
    >>> a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level",\
    'ids': [1, 2, 3] }
    >>> print_sorted_dictionary(a_dictionary)
    Number: 89
    ids: [1, 2, 3]
    language: C
    track: Low level
    """
    if a_dictionary == {}:
        print(" : ")
    else:
        for k in sorted(a_dictionary.keys()):
            print(f"{k}: {a_dictionary[k]}")
