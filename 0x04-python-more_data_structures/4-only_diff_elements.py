#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set.

    Args:
    set_1 (set) : first set
    set_2 (set) : second set

    Returns:
    (set) : a new set that contains all elements present in
    only one set.

    Examples:
    >>> set_1 = { "Python", "C", "Javascript" }
    >>> set_2 = { "Bash", "C", "Ruby", "Perl" }
    >>> od_set = only_diff_elements(set_1, set_2)
    >>> print(sorted(list(od_set)))
    ['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
    """
    return (set_1 - set_2) | (set_2 - set_1)
