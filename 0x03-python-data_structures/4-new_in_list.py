#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position
    without modifying the original list.

    Args:
    my_list (list) : original list
    idx (int) : index
    element (any) : element to insert in list

    Returns:
    (list) : a new list with `element` at index `idx` replaced.

    if `idx` is negative or out of range return a copy of the original list.

    Examples:
    >>> my_list = [1, 2, 3, 4, 5]
    >>> idx = 3
    >>> new_element = 9
    >>> new_list = new_in_list(my_list, idx, new_element)
    >>> print(new_list)
    [1, 2, 3, 9, 5]
    >>> print(my_list)
    [1, 2, 3, 4, 5]
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_list = []
        new_list.extend(my_list)
        new_list[idx] = element
        return new_list
