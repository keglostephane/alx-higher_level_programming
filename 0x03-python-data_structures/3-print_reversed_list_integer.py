#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse order

    Args:
    my_list (list) : list of integers

    Returns:
    None

    Example:
    >>> my_list = [1, 2, 3, 4, 5]
    >>> print_reversed_list_integer(my_list)
    5
    4
    3
    2
    1
    """
    if my_list is None:
        return None
    else:
        for i in my_list[::-1]:
            print("{:d}".format(i))
