#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another
    in a new list.

    Args:
    my_list (list) : list of elements
    search (any) : element to replace in the list
    replace (any): new element to insert

    Returns:
    (list) : a new list with all occurences of `search`
    replaced by `replace`.

    Examples:
    >>> my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    >>> new_list = search_replace(my_list, 2, 89)
    >>> print(new_list)
    [1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
    >>> print(my_list)
    [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    """
    if my_list == []:
        return []
    elif my_list.count(search) == 0:
        return my_list
    else:
        return [replace if elem == search else elem for elem in my_list]
