#!/usr/bin/python3
"""9-stdudent

This module provide ``Student`` class that represent a student.
"""


class Student:
    """Represent a student.

    :param first_name: first name of the student
    :type first_name: str
    :param last_name: last name of the student
    :type last_name: str
    :param age: age of the student
    :type age: int
    """
    def __init__(self, first_name, last_name, age):
        """initializer"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return dictionary representation"""
        return self.__dict__
