#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """ prints `x` elements of a list.

    :param my_list: list of elements, defaults to []
    :type my_list: list, optional
    :param x: number of elements to print, defaults to 0
    :type x: int
    :return: the number of elements printed
    :rtype: int
    """
    if x <= 0:
        print("")
        return 0
    try:
        p = 0
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            p += 1
        print("")
    except IndexError:
        print("")

    return p
