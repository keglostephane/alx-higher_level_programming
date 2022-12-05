#!/usr/bin/python3
def no_c(my_string):
    """Removes all characters c and C from a string.

    Args:
    my_string (str)

    Returns:
    (str) : a copy of `my_string` with `c` and 'C' removed.

    Examples:
    >>> print(no_c("Best School"))
    Best Shool
    >>> print(no_c("Chicago"))
    hiago
    >>> print(no_c("C is fun!"))
     is fun!
    """
    if my_string == "":
        return ""
    else:
        new_string = ""
        for c in my_string:
            if c not in "cC":
                new_string += c
        return new_string
