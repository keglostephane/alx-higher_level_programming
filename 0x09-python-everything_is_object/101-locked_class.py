#!/usr/bin/python3
"""LockedClass Module
"""


class LockedClass:
    """A Locked class that prevents user from creating
    dynamically new instances attributes except if
    the new instance attribute is called ``first_name``
    """
    __slots__ = ("first_name",)
