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

        # test with expected data
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

    def testFromJSONStringToList(self):
        """Test from_json_string() returns the original list of dictionary"""
        # json_string is None or empty
        json_string = None
        expected = []
        self.assertEqual(Base.from_json_string(json_string), expected)

        json_string = ""
        expected = []
        self.assertEqual(Base.from_json_string(json_string), expected)

        # test with expected data
        json_string = "[]"
        expected = []
        self.assertEqual(Base.from_json_string(json_string), expected)

        json_string = '[{"size": 12, "x": 1, "y": 0, "id":10}]'
        expected = [{'size': 12, 'x': 1, 'y': 0, 'id': 10}]
        self.assertEqual(Base.from_json_string(json_string), expected)

        json_string = ('[{"width": 16, "height": 19, "x": 1, "y": 1, "id": 0}'
                       ', {"size": 64, "x": 0, "y": 1, "id": 18}]')
        expected = [{'width': 16, 'height': 19, 'x': 1, 'y': 1, 'id': 0},
                    {'size': 64, 'x': 0, 'y': 1, 'id': 18}]
        self.assertEqual(Base.from_json_string(json_string), expected)

        # test with wrong data
        with self.assertRaises(json.decoder.JSONDecodeError):
            json_string = "{'size': 15, 'id': 12}"
            Base.from_json_string(json_string)

        with self.assertRaises(json.decoder.JSONDecodeError):
            json_string = "{1, 2, 3}"
            Base.from_json_string(json_string)

    def testCreateFromDict(self):
        """ Test the creation of a Base instance from a dictionary."""
        # test class with empty dictionary
        rect = Rectangle.create()
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 1)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

        square = Square.create()
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

        # test if instances created are unique
        square1 = Square(4, 1, 2, 1)
        square2 = square1.create(size=4, x=1, y=2, id=1)
        square3 = Square.create(size=4, x=1, y=2, id=1)
        self.assertNotEqual(id(square1), id(square2))
        self.assertNotEqual(id(square1), id(square3))

        # test with expected data
        rect1 = Rectangle(15, 12)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(width=15, height=12)
        rect2_dict = rect2.to_dictionary()
        self.assertNotEqual(rect1_dict, rect2_dict)
        self.assertNotEqual(rect1, rect2)

        square1 = Square(25, 0, 1, 5)
        square2 = Square.create(**{'size': 25, 'x': 0, 'y': 1, 'id': 5})
        s1_dict = square1.to_dictionary()
        s2_dict = square2.to_dictionary()
        self.assertEqual(s1_dict, s2_dict)
        self.assertNotEqual(square1, square2)

        square = Square.create(id=5)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

        rect = Rectangle.create(x=0, y=0)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 1)

        # test with wrong data
        with self.assertRaises(TypeError):
            square = Square.create(size=2.5, x=1, y=2, id=1)

        with self.assertRaises(ValueError):
            rectangle = Rectangle.create(width=15, height=0, x=1, y=2)

    def testLoadFromFile(self):
        """Test load_from_file() returns a list of instance"""

        import os

        # missing json file
        cls = Rectangle
        filename = f"{cls.__name__}.json"
        if os.path.exists(filename):
            os.remove(filename)
        self.assertFalse(os.path.exists(filename))
        expected = []
        self.assertEqual(cls.load_from_file(), expected)

        # json file exists and content is an empty list
        cls = Square
        filename = f"{cls.__name__}.json"
        cls.save_to_file([])
        expected = []
        self.assertTrue(os.path.exists(filename))
        self.assertEqual(cls.load_from_file(), [])
        os.remove(filename)

        # json file exists and contains two Square objects
        cls = Square
        filename = f"{cls.__name__}.json"
        square1 = cls(12, 1, 1, 0)
        square2 = cls(50, 0, 1, 1)
        list_objs = [square1, square2]
        cls.save_to_file(list_objs)
        list_inst = cls.load_from_file()
        os.remove(filename)
        self.assertEqual(len(list_objs), len(list_inst))
        self.assertNotEqual(list_objs[0], list_inst[0])
        self.assertEqual(list_objs[0].__str__(), list_inst[0].__str__())
        self.assertNotEqual(square2, list_inst[1])
        self.assertEqual(list_objs[0].__str__(), list_inst[0].__str__())
        self.assertIsInstance(list_inst[0], cls)
        self.assertIsInstance(list_inst[1], cls)

        # json file exists and contains two Rectangle objects
        cls = Rectangle
        filename = f"{cls.__name__}.json"
        rect1 = cls(12, 10)
        rect2 = cls(10, 12)
        list_objs = [rect1, rect2]
        cls.save_to_file(list_objs)
        list_inst = cls.load_from_file()
        os.remove(filename)
        self.assertTrue(len(list_objs), len(list_inst))
        self.assertNotEqual(list_objs[0], list_inst[0])
        self.assertEqual(list_objs[0].__str__(), list_inst[0].__str__())
        self.assertNotEqual(list_objs[1], list_inst[1])
        self.assertEqual(list_objs[1].__str__(), list_inst[1].__str__())
        self.assertIsInstance(list_inst[0], cls)
        self.assertIsInstance(list_inst[1], cls)

        # json file exits and contain invalid data
        # mixed Square and Rectangle instances
        cls = Square
        filename = f"{cls.__name__}.json"
        square = cls(16)
        rect = Rectangle(18, 15)
        list_objs = [square, rect]
        cls.save_to_file(list_objs)
        list_inst = cls.load_from_file()
        os.remove(filename)
        self.assertEqual(len(list_objs), len(list_inst))
        self.assertNotEqual(list_objs[0], list_inst[0])
        self.assertEqual(list_objs[0].__str__(), list_inst[0].__str__())
        self.assertNotEqual(list_objs[1], list_inst[1])
        self.assertNotEqual(list_objs[1].__str__(), list_inst[1].__str__())
        self.assertIsInstance(list_inst[0], cls)
        self.assertIsInstance(list_inst[1], cls)

        # Square and str instances
        cls = Square
        filename = f"{cls.__name__}.json"
        square = cls(12)
        string = "Hello"
        list_objs = [square, string]
        with self.assertRaises(AttributeError):
            cls.save_to_file(list_objs)
            list_inst = cls.load_from_file()
