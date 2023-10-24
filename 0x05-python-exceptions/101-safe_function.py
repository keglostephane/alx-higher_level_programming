#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Execute a function safely.

    :param func: function pointer
    :type func: function
    :param args: positional arguments
    :type args: tuple
    :return: the result of the function or None if something happens during
        function execution.
    :rtype: any
    """
    try:
        return fct(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
