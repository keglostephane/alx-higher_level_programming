#!/usr/bin/python3
"""Unittest for Rectangle class
"""
import unittest
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
