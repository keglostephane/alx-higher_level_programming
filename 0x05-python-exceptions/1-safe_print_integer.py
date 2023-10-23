#!/usr/bin/python3

def safe_print_integer(value):
    """prints an integer

    :param value: an integer
    :type value: int
    :return: True if `value` has been printed, otherwise retuns False
    :rtype: bool
    """
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    return True
