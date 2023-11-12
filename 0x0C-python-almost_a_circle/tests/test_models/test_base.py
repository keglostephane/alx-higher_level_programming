#!/usr/bin/python3
"""Unittest for Base class
"""
import unittest
from models.base import Base


class testBase(unittest.TestCase):
    """Test the Base class"""

    def testIsBaseInstance(self):
        """Test if an object is an instance of Base class"""
        base = Base()
        base2 = Base(2)
        self.assertIsInstance(base, Base)
        self.assertIsInstance(base2, Base)

    def testBaseInstanceIdAttributeValue(self):
        """Test id attribute value of differents instance of Base class"""
        base10 = Base(10)
        base_n = Base(-5)
        base = Base()
        self.assertEqual(base10.id, 10)
        self.assertEqual(base_n.id, -5)
        self.assertEqual(base.id, 1)

    def testBasePrivateClassAttribte(self):
        """Test if Base class has private attribute(s)"""
        base7 = Base(7)
        self.assertIn("_Base__nb_objects", Base.__dict__)
        self.assertNotIn("__nb_objects", base7.__dict__)

    def testCreateBaseInstanceWithInvalidNumberArguments(self):
        """Create a Base instance with an invalid number of arguments."""
        with self.assertRaises(TypeError) as error:
            base = Base(2, 3)
        self.assertEqual(str(error.exception),
                         "__init__() takes from 1 to 2 positional arguments"
                         " but 3 were given")
