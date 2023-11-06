#!/usr/bin/python3
"""1-my_list

This module provide ``MyList`` class that inherits from ``List``.
"""


class MyList(list):
    """A class that inherits from ``list``.
    """
    def print_sorted(self):
        """Print the list in ascending order.
        """
        print(sorted(self))
