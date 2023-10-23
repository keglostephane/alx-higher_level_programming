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
        return True
    except (ValueError, TypeError):
        return False
