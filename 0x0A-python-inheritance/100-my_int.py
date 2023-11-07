#!/usr/bin/python3
"""100-my_int

This module provide ``MyInt`` class that inherits from ``int``
"""


class MyInt(int):
    """A Rebel int subclass.

    :param value: MyInt value
    :type value: int
    :raise TypeError: value must be an integer
    """
    def __init__(self, value):
        """Initializer"""
        if type(value) is not int:
            raise TypeError("value must be an integer")

        self.value = value

    def __eq__(self, obj):
        """Test if ``MyInt`` object is not equal to another object.

        :param obj: an object
        :type obj: int, float, bool
        :return: True if ``MyInt`` object is not equal to ``obj``
        :rtype: bool
        """
        return self.value != obj

    def __ne__(self, obj):
        """ Test if ``MyInt`` object is equal to another object.

        :param obj: an object
        :type obj: int, float, bool
        :return: True if ``MyInt`` object is equal to ``obj``
        :rtype: bool
        """
        return self.value == obj
