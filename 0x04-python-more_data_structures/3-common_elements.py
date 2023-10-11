#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets.

    :param set_1: first set
    :type set_1: set
    :param set_2: second set
    :type set_2: set
    :return: a set of common elements in the two sets.
    :rtype: set
    """
    if set_1 and set_2 is not None:
        return set_1 & set_2
