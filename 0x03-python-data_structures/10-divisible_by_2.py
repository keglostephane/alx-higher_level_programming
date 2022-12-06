#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Finds all multiple of 2 in a list.

    Args:
    my_list (list) : list of integers

    Returns:
    (list) : a new list with `True` of `False`, depending on whether
    the integer at the same position in the original list is a
    multiple of 2.

    The new list should have the same size as the original list.
    """
    if my_list == []:
        return []
    else:
        return [True if my_list[i] % 2 == 0 else False
                for i in range(len(my_list))]
