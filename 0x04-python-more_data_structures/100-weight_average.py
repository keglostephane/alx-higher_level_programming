#!/usr/bin/python3
def weight_average(my_list=[]):
    """Return the weighted average of all integers tuple.

    :param my_list: a list of tuples, defaults to []
    :type my_list: list, optional
    :return: the weighted average of all integers tuple.
        0 if the list is empty
    :rtype: int, float
    """
    if my_list is []:
        return 0

    sum = 0
    weight = 0

    for a, b in my_list:
        sum += a * b
        weight += b
    return sum / weight
