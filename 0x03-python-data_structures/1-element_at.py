#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieve an element from a list

    Parameters:
    my_list (list): list
    idx (int): given index to retrieve an element

    Returns:
    my_list[idx] : element of `my_list` at index `idx`.

    None: if `idx` is negative or out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
