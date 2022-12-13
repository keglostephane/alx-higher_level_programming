#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple
    (<score>, <weight>)

    Args:
    my_list (list)

    Returns:
    (float) : the weighted average

    Examples:
    >>> my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    >>> result = weight_average(my_list)
    >>> print("Average: {:0.2f}".format(result))
    Average: 2.80
    """
    if my_list == []:
        return 0
    else:
        marks = 0       # a mark equal to a score multiplied by its weight
        total_weight = 0
        for score, weight in my_list:
            marks += score * weight
            total_weight += weight
        return marks / total_weight
