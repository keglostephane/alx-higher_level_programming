#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the biggest integer of a list.

    Args:
    my_list (list) : integer list

    Returns:
    (int) : biggest integer in a list of integers.

    Examples:
    >>> my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    >>> max_value = max_integer(my_list)
    >>> print("Max: {}".format(max_value))
    Max: 90
    """
    if my_list == []:
        return None
    else:
        new_list = sorted(my_list)
        return new_list[-1]
