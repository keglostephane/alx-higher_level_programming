#!/usr/bin/python3
"""Unittest for Base class
"""
import unittest
import json
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


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

        list_dict = []
        square1_dict = Square(25, 1, 2, 5).to_dictionary()
        square2_dict = Square(10, 0, 5, 3).to_dictionary()
        list_dict.append(square1_dict)
        list_dict.append(square2_dict)
        expected = ('[{"size": 25, "x": 1, "y": 2, "id": 5}, '
                    '{"size": 10, "x": 0, "y": 5, "id": 3}]')
        origin = json.loads(expected)
        self.assertEqual(Base.to_json_string(list_dict), expected)
        self.assertEqual(origin, list_dict)

        list_dict = []
        square_dict = Square(50, 12, 10, 6).to_dictionary()
        rectangle_dict = Rectangle(12, 8, 1, 2, 3).to_dictionary()
        list_dict.append(square_dict)
        list_dict.append(rectangle_dict)
        expected = ('[{"size": 50, "x": 12, "y": 10, "id": 6}, '
                    '{"width": 12, "height": 8, "x": 1, "y": 2, "id": 3}]')
        origin = json.loads(expected)
        self.assertEqual(Base.to_json_string(list_dict), expected)
        self.assertEqual(origin, list_dict)

        list_dict = []
        square_dict = Square(10, 0, 0, 1).to_dictionary()
        invalid_dict = {1, 2, 3}
        list_dict.append(square_dict)
        list_dict.append(invalid_dict)
        self.assertRaises(TypeError, Base.to_json_string, list_dict)

    def testSaveJSONToFile(self):
        """Test writing JSON representation of list of objects to a file."""

        import os

        # list of object is None or empty
        list_objs = None
        cls = Rectangle
        cls.save_to_file(list_objs)
        filename = f"{cls.__name__}.json"
        with open(filename, encoding='utf-8') as fp:
            content = fp.read()
        os.remove(filename)
        expected = "[]"
        self.assertEqual(content, expected)

        list_objs = []
        cls = Square
        cls.save_to_file(list_objs)
        filename = f"{cls.__name__}.json"
        with open(filename, encoding='utf-8') as fp:
            content = fp.read()
        os.remove(filename)
        expected = "[]"
        self.assertEqual(content, expected)

        # the destination file exists
        cls = Rectangle
        list_objs = [Rectangle(4, 3, 1, 2, 0), Square(10, 1, 2, 3)]
        cls.save_to_file(list_objs)
        filename = f"{cls.__name__}.json"
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)

        cls = Square
        cls.save_to_file(list_objs)
        filename = f"{cls.__name__}.json"
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)

        # destination file is overwritten if it already exists
        cls = Rectangle
        obj1 = Rectangle(3, 4)
        obj2 = Square(10)
        filename = f"{cls.__name__}.json"
        cls.save_to_file([obj1, obj2])
        with open(filename, encoding='utf-8') as fp:
            data1 = fp.read()
        cls.save_to_file([obj1])
        with open(filename, encoding='utf-8') as fp:
            data2 = fp.read()
        self.assertLess(len(data2), len(data1))

        # test the expected data
        cls = Square
        obj1 = Square(25, 12, 3, 1)
        obj2 = Rectangle(12, 9, 1, 2, 3)
        list_objs = [obj1, obj2]
        filename = f"{cls.__name__}.json"
        cls.save_to_file(list_objs)
        with open(filename, encoding='utf-8') as fp:
            data = fp.read()
        expected = ('[{"size": 25, "x": 12, "y": 3, "id": 1}, '
                    '{"width": 12, "height": 9, "x": 1, "y": 2, "id": 3}]')
        self.assertEqual(data, expected)
        os.remove(filename)

        # test with wrong data
        cls = Square
        obj1 = Rectangle(2, 1)
        obj2 = "Hello"
        list_objs = [obj1, obj2]
        with self.assertRaises(AttributeError):
            cls.save_to_file(list_objs)
