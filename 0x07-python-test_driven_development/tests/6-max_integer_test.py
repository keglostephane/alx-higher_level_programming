#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test for the max integer in a list of integers"""

    def testMissingArgument(self):
        """Calling max_integer() with no argument"""
        self.assertEqual(max_integer(), None)

    def testEmptyList(self):
        """Calling max_integer() with an empty list"""
        self.assertEqual(max_integer([]), None)

    def testListWithOneInteger(self):
        """Calling max_integer() with a list of one integer"""
        self.assertEqual(max_integer([1]), 1)

    def testListWithMultipleIntegers(self):
        """Calling max_integer() with a list of multiple integers"""
        positive = [5, 8, 1, 0]
        negative = [-4, -2, -8, -10]
        integers = [-2, -6, 10, 3]
        floats = [2, 1.8, 1.9, 2.0]
        self.assertEqual(max_integer(positive), 8)
        self.assertEqual(max_integer(negative), -2)
        self.assertEqual(max_integer(integers), 10)
        self.assertEqual(max_integer(floats), 2.0)

    def testListWithMixedValues(self):
        """Calling max_integer() with a list of mixed values"""
        mixed = [2, 0, 7, "3"]
        self.assertRaises(TypeError, max_integer, mixed)

    def testWithTuple(self):
        """Calling max_integer() with a tuple"""
        t1 = tuple([7, 3, 5])
        self.assertEqual(max_integer(t1), 7)

    def testWithSet(self):
        """Calling max_integer() with a set"""
        s1 = set([7, 3, 5])
        self.assertRaises(TypeError, max_integer, s1)
