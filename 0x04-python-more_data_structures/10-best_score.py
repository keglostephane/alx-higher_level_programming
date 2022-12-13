#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value.

    Args:
    a_dictionary (dict) : a dictionary

    Returns:
    (any immutable) :  the key with biggest value in the dictionary.

    If no score found, return None.
    """
    if a_dictionary is None:
        return None
    else:
        return max(a_dictionary, key=lambda x: a_dictionary[x],
                   default=None)
