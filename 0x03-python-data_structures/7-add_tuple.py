#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples.

    Args:
    tuple_a (tuple) : first tuple
    tuple_b (tuple) : second tuple

    Returns:
    (tuple) : a tuple with 2 integers

    The first element should be the addition of the first element
    of each argument.

    The second element should be the addition of the second element
    of each arguement.

    If a tuple is smaller than 2, use the value 0 for each missing
    argument.

    if a tuple is bigger than 2, use only the first 2 integers.

    Examples:
    >>> tuple_a = (1, 89)
    >>> tuple_b = (88, 11)
    >>> new_tuple = add_tuple(tuple_a, tuple_b)
    >>> print(new_tuple)
    (89, 100)
    >>> print(add_tuple(tuple_a, (1, )))
    (2, 89)
    >>> print(add_tuple(tuple_a, ()))
    (1, 89)
    """
    new_tuple = ()
    sum = 0
    for i in range(2):
        try:
            sum += tuple_a[i]
        except IndexError:
            sum += 0
        try:
            sum += tuple_b[i]
        except IndexError:
            sum += 0
        new_tuple += (sum,)
        sum = 0

    return new_tuple
