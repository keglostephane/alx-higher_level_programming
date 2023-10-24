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
    except (ValueError, TypeError) as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return False
