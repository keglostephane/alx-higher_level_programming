#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Returns a list with all values multiplied by a number
    without using any loops.

    Args:
    my_list (list)
    number (int|float)

    Returns:
    (list) : a new list with same length as `my_list` where each value
    is multiplied by `number`.

    Examples:
    >>> my_list = [1, 2, 3, 4, 6]
    >>> new_list = multiply_list_map(my_list, 4)
    >>> print(new_list)
    [4, 8, 12, 16, 24]
    >>> print(my_list)
    [1, 2, 3, 4, 6]
    """
    return [num for num in map(lambda x: x*number, my_list)]
