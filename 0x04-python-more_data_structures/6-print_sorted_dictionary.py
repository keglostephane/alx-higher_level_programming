#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys.

    :param a_dictionary: a dictionary
    :type a_dictionary: dict
    """
    if a_dictionary is not None:
        for key, value in sorted(a_dictionary.items()):
            print("{}: {}".format(key, value))
