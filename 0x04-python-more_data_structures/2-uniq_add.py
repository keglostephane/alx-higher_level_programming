#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list
    only once for each integer.

    Args:
    my_list (list) : list of integers

    Returns:
    (int) : sum of unique integers in the list

    Examples:
    >>> my_list = [1, 2, 3, 1, 4, 2, 5]
    >>> result = uniq_add(my_list)
    >>> print("Result: {:d}".format(result))
    Result: 15
    """
    if my_list == []:
        return []
    else:
        sum = 0
        uniq = set(my_list)
        for num in uniq:
            sum += num
        return sum
