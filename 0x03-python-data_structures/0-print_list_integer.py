#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print all integers of a list.

    Args:
    my_list (list) : list of integers

    Returns:
    None

    >>> my_list = [1, 2, 3, 4, 5]
    >>> print_list_integer(my_list)
    1
    2
    3
    4
    5
    """
    for num in my_list:
        print("{:d}".format(num))
