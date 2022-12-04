#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position.

    Args:
    my_list (list): list
    idx (int): given index to insert an element
    element (any): element to insert

    Returns:
    (list) : `my_list` included element `element` added at index `idx`.

    If `idx` is negative or out of range returns the original list.

    Examples:
    >>> my_list = [1, 2, 3, 4, 5]
    >>> idx = 3
    >>> new_element = 9
    >>> new_list = replace_in_list(my_list, idx, new_element)
    >>> print(new_list)
    [1, 2, 3, 9, 5]
    >>> print(my_list)
    [1, 2, 3, 9, 5]
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
