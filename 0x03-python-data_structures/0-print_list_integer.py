#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print all integers of a list

    Parameters:
    my_list (list) : list of integers

    Returns:
    None

    Example:
    >>> my_list = [1, 2, 3, 4, 5]
    >>> print_list_integer(my_list)
    """
    for num in my_list:
        print(num)
