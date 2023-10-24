#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Print an integer.

    :param value: integer value to print
    :type value: int
    :return: True if `value` has been correctly printed, False otherwise.
    :rtype: bool
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError as error:
        sys.stderr.write("Exception: {}\n".format(error))
        return False
