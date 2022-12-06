#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list

    Args:
    my_list (list)
    idx (int): index

    Returns:
    (list): a lis with item at position `idx` deleted

    if `idx` is negative or out of range, nothing change.

    Examples:
    >>> my_list = [1, 2, 3, 4, 5]
    >>> idx = 3
    >>> new_list = delete_at(my_list, idx)
    >>> print(new_list)
    [1, 2, 3, 5]
    >>> print(my_list)
    [1, 2, 3, 5]
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        del my_list[idx]
        return my_list
