#!/usr/bin/python3
"""Unittest for Square class
"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    """Test Square Class"""

    def testIsSquareInstance(self):
        """Test if an object is an instance of Square class"""
        square = Square(5)
        self.assertIsInstance(square, Rectangle)

    def testIsRectangleSubclass(self):
        """Test if Square inherits from Rectangle class"""
        self.assertTrue(issubclass(Square, Rectangle))

    def testIsBaseSubclass(self):
        """Test if Square inherits from Base class"""
        self.assertTrue(issubclass(Square, Base))

    def testCreateSquareWithAllArguments(self):
        """Test create Square with all arguments"""
        square = Square(4, 1, 1, 1)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 1)
        self.assertEqual(square.width, 4)
        self.assertEqual(square.height, 4)

    def testCreateSquareWithMissingArguments(self):
        """Test create Sqaure with missing arguments"""
        # Missing required size argument
        self.assertRaises(TypeError, Square)
        # Missing optional arguments
        self.assertTrue(Square(5))

    def testCreateSquareWithInvalidArguments(self):
        """Test create Square with invalid arguments"""
        # incorrect size argument
        with self.assertRaises(TypeError) as error:
            square = Square("3", 0, 0, 1)
        self.assertEqual(str(error.exception), "width must be an integer")

        with self.assertRaises(ValueError) as error:
            square = Square(0, 0, 0, 1)
        self.assertEqual(str(error.exception), "width must be > 0")

        # incorrect x, y arguments
        with self.assertRaises(TypeError) as error:
            square = Square(8, 2.5, 0, 1)
        self.assertEqual(str(error.exception), "x must be an integer")

        with self.assertRaises(TypeError) as error:
            square = Square(12, 3, "3", 1)
        self.assertEqual(str(error.exception), "y must be an integer")

        with self.assertRaises(ValueError) as error:
            square = Square(5, -2, 0, 1)
        self.assertEqual(str(error.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as error:
            square = Square(12, 6, -7, 1)
        self.assertEqual(str(error.exception), "y must be >= 0")

    def testSquareArea(self):
        """Test Square area"""
        square = Square(18)
        self.assertEqual(square.area(), 324)

        square = Square(3, 1, 3, 1)
        self.assertEqual(square.area(), 9)

    def testSquareDisplay(self):
        """Test Square printing"""
        with patch('sys.stdout', new_callable=StringIO) as output:
            square = Square(4)
            square.display()
        result = output.getvalue()
        expected = ("####\n"
                    "####\n"
                    "####\n"
                    "####\n")
        print("\nCalling display() method of Square(4)")
        print(result)
        self.assertEqual(result, expected)

        with patch('sys.stdout', new_callable=StringIO) as output:
            square = Square(3, 1, 1, 5)
            square.display()
        result = output.getvalue()
        expected = ("\n"
                    " ###\n"
                    " ###\n"
                    " ###\n")
        print("\nCalling display() method of Square(3, 1, 1, 5)")
        print(result)
        self.assertEqual(result, expected)

        with patch('sys.stdout', new_callable=StringIO) as output:
            square = Square(7, 5, 2, 3)
            square.display()
        result = output.getvalue()
        expected = ("\n"
                    "\n"
                    "     #######\n"
                    "     #######\n"
                    "     #######\n"
                    "     #######\n"
                    "     #######\n"
                    "     #######\n"
                    "     #######\n")
        print("\nCalling display() method of Square(7, 5, 2, 3)")
        print(result)
        self.assertEqual(result, expected)

    def testSquareStr(self):
        """Test human readable representation of Square"""
        with patch('sys.stdout', new_callable=StringIO) as output:
            square = Square(12, 3, 4, 2)
            print(square)
        result = output.getvalue()
        expected = "[Square] (2) 3/4 - 12\n"
        print("\nCalling str() method of Square(12, 3, 4, 2)")
        print(result)
        self.assertEqual(result, expected)

        with patch('sys.stdout', new_callable=StringIO) as output:
            square = Square(9, 0, 0, 0)
            print(square)
        result = output.getvalue()
        expected = "[Square] (0) 0/0 - 9\n"
        print("\nCalling str() method of Square(9, 0, 0, 0)")
        print(result)
        self.assertEqual(result, expected)
