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
        self.assertRaises(TypeError, Base, 2, 3)

    def testListDictionaryToJsonString(self):
        """Test JSON string representation of a list of dictionary"""
        list_dict = None
        json_str = Base.to_json_string(list_dict)
        self.assertEqual(json_str, "[]")

        list_dict = []
        json_str = Base.to_json_string(list_dict)
        self.assertEqual(json_str, "[]")

        list_dict = [{'a': 1, 'b': True, 'c': -7.2}]
        json_str = '[{"a": 1, "b": true, "c": -7.2}]'
        self.assertEqual(Base.to_json_string(list_dict), json_str)

        list_dict = [{'a': 2, 'c': ['Hello', 'ALX']}, {'a': True, 'b': None}]
        json_str = '[{"a": 2, "c": ["Hello", "ALX"]}, {"a": true, "b": null}]'
        self.assertEqual(Base.to_json_string(list_dict), json_str)

        list_dict = [["hello", "world"], [{"hello": 5, "world": 5}]]
        json_str = '[["hello", "world"], [{"hello": 5, "world": 5}]]'
        self.assertEqual(Base.to_json_string(list_dict), json_str)

        list_dict = [{1, 2, 3}]
        with self.assertRaises(TypeError) as error:
            Base.to_json_string(list_dict)
            self.assertEqual(str(error.exception),
                             ("Object of type set "
                              "is not JSON serializable"))

        list_dict = [{'a': 10, 'b': (1, 2, 3)}]
        json_str = '[{"a": 10, "b": [1, 2, 3]}]'
        self.assertEqual(Base.to_json_string(list_dict), json_str)
