#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """prints the first `x` elements of a list and only integers.

    :param my_list: a list, defaults to []
    :type my_list: list, optional
    :param x: number of elements in the list, defaults to 0
    :type x: int, optional
    :return: the number of integers printed
    :rtype: int
    """
    try:
        p = 0
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                p += 1
        print("")
        return p
    except (TypeError, ValueError):
        pass
