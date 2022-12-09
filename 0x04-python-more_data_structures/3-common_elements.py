#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets.

    Args:
    set_1 (set) : first set
    set_2 (set) : second set

    Returns:
    (set) : common elements in the two sets

    Examples:
    >>> set_1 = { "Python", "C", "Javascript" }
    >>> set_2 = { "Bash", "C", "Ruby", "Perl" }
    >>> c_set = common_elements(set_1, set_2)
    >>> print(sorted(list(c_set)))
    ['C']
    """
    return set_1 & set_2
