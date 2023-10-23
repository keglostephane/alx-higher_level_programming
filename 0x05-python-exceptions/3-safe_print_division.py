#!/usr/bin/python3

def safe_print_division(a, b):
    """Divides 2 integers and prints the result.

    :param a: first integer
    :type a: int
    :param b: second integer
    :type b: int
    :return: the value of the division otherwise None
    :rtype: float
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        if result is None:
            print("Inside result: {}".format(result))
        else:
            print("Inside result: {:.1f}".format(result))
        return result
