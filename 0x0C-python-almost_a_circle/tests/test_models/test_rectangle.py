#!/usr/bin/python3
"""Unittest for Rectangle class
"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test Rectangle Class"""

    def testIsRectangleInstance(self):
        """Test if an object is an instance of Rectangle class"""
        rect = Rectangle(3, 2)
        self.assertIsInstance(rect, Rectangle)

    def testIsBaseSubclass(self):
        """Test if Rectangle class inherits from Base class"""
        self.assertTrue(issubclass(Rectangle, Base))

    def testRectanglePrivateInstanceAttribute(self):
        """Test if Rectangle instances have private attributes"""
        rect = Rectangle(1, 2)
        self.assertIn("_Rectangle__width", rect.__dict__)
        with self.assertRaises(AttributeError):
            rect.__width

        self.assertIn("_Rectangle__height", rect.__dict__)
        with self.assertRaises(AttributeError):
            rect.__height

        self.assertIn("_Rectangle__x", rect.__dict__)
        with self.assertRaises(AttributeError):
            rect.__x

        self.assertIn("_Rectangle__y", rect.__dict__)
        with self.assertRaises(AttributeError):
            rect.__x

    def testCreateRectangleWithAllArguments(self):
        """Test create Rectangle with all arguments"""
        rect = Rectangle(7, 5, 3, 2, 1)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 1)

    def testCreateRectangleWithMissingRequiredArguments(self):
        """Test create Rectangle with missing arguments"""
        # Missing width and height arguments
        self.assertRaises(TypeError, Rectangle)
        # Missing height argument
        self.assertRaises(TypeError, Rectangle, 7)

    def testCreateRectangleWithIncorrectArguments(self):
        """Test create Rectangle with invalid arhuments"""
        with self.assertRaises(TypeError) as error:
            rect = Rectangle("3", 5)
        self.assertEqual(str(error.exception), "width must be an integer")

        with self.assertRaises(TypeError) as error:
            rect = Rectangle(3, "5")
        self.assertEqual(str(error.exception), "height must be an integer")

        with self.assertRaises(TypeError) as error:
            rect = Rectangle(3, 5, 1.5, 1)
        self.assertEqual(str(error.exception), "x must be an integer")

        with self.assertRaises(TypeError) as error:
            rect = Rectangle(4, 5, 2, 3.5)
        self.assertEqual(str(error.exception), "y must be an integer")

        with self.assertRaises(ValueError) as error:
            rect = Rectangle(0, 5)
        self.assertEqual(str(error.exception), "width must be > 0")

        with self.assertRaises(ValueError) as error:
            rect = Rectangle(3, 0)
        self.assertEqual(str(error.exception), "height must be > 0")

        with self.assertRaises(ValueError) as error:
            rect = Rectangle(8, 5, -1, 2)
        self.assertEqual(str(error.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as error:
            rect = Rectangle(9, 6, 1, -3)
        self.assertEqual(str(error.exception), "y must be >= 0")

    def testRectangleArea(self):
        """Test Rectangle's area computation"""
        rect = Rectangle(7, 4)
        self.assertEqual(rect.area(), 28)

        rect = Rectangle(7, 7, 1, 1, 2)
        self.assertEqual(rect.area(), 49)

        rect = Rectangle(8, 9, 9, 8, 0)
        self.assertEqual(rect.area(), 72)

    def testRectanglePrint(self):
        """Test printing Rectangle"""
        with patch('sys.stdout', new_callable=StringIO) as output:
            rect = Rectangle(4, 3)
            rect.display()
        result = output.getvalue()
        expected = ("####\n"
                    "####\n"
                    "####\n")
        print('\n' + result)
        self.assertEqual(result, expected)

        with patch('sys.stdout', new_callable=StringIO) as output:
            rect = Rectangle(1, 1)
            rect.display()
        result = output.getvalue()
        expected = ("#\n")
        print('\n' + result)
        self.assertEqual(result, expected)

        with patch('sys.stdout', new_callable=StringIO) as output:
            rect = Rectangle(2, 3)
            rect.display()
        result = output.getvalue()
        expected = ("##\n"
                    "##\n"
                    "##\n")
        print('\n' + result)
        self.assertEqual(result, expected)

    def testRectangleAsStr(self):
        """Test human readable representation of Rectangle"""
        with patch('sys.stdout', new_callable=StringIO) as output:
            rect = Rectangle(4, 3, 2, 1, 0)
            print(rect)
        result = output.getvalue()
        expected = "[Rectangle] (0) 2/1 - 4/3\n"
        print('\n' + result)
        self.assertEqual(result, expected)

        with patch('sys.stdout', new_callable=StringIO) as output:
            rect = Rectangle(1, 5, 0, 0, 6)
            print(rect)
        result = output.getvalue()
        expected = "[Rectangle] (6) 0/0 - 1/5\n"
        print('\n' + result)
        self.assertEqual(result, expected)
