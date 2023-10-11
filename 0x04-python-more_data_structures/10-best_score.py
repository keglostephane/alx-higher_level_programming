#!/usr/bin/python3
def best_score(a_dictionary):
    """Return the key with the biggest integer value.

    :param a_dictionary: a dictionary
    :type a_dictionary: dict
    :return: the key with the biggest integer value
        if no score found, return None
    :rtype: str
    """
    if a_dictionary is None:
        return None
    return max(a_dictionary)
