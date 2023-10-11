#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set.

    :param set_1: first set
    :type set_1: set
    :param set_2: second set
    :typr set_2: set
    :return: a set of all elements present in only one set.
    :rtype: set
    """
    return set_1.symmetric_difference(set_2)
