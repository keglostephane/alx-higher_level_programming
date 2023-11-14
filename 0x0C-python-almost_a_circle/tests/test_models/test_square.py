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
            self.assertEqual(result, expected)

        with patch('sys.stdout', new_callable=StringIO) as output:
            square = Square(3, 1, 1, 5)
            square.display()
            result = output.getvalue()
            expected = ("\n"
                        " ###\n"
                        " ###\n"
                        " ###\n")
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
            self.assertEqual(result, expected)

    def testSquareStr(self):
        """Test human readable representation of Square"""
        with patch('sys.stdout', new_callable=StringIO) as output:
            square = Square(12, 3, 4, 2)
            print(square)
            result = output.getvalue()
            expected = "[Square] (2) 3/4 - 12\n"
            self.assertEqual(result, expected)

        with patch('sys.stdout', new_callable=StringIO) as output:
            square = Square(9, 0, 0, 0)
            print(square)
            result = output.getvalue()
            expected = "[Square] (0) 0/0 - 9\n"
            self.assertEqual(result, expected)

    def testSquareWidthHeightValidation(self):
        """Test Square width and height validation"""
        square = Square(5, 1, 2, 0)
        self.assertNotIn("size", square.__dict__)
        self.assertNotIn("_Square__size", square.__dict__)

        with self.assertRaises(TypeError) as error:
            square = Square(2.5)
            self.assertEqual(str(error.exception), "width must be an integer")

        with self.assertRaises(ValueError) as error:
            square = Square(-2)
            self.assertEqual(str(error.exception), "width must be > 0")

        square.size = 10
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def testSquareUpdateWithPositionalArguments(self):
        """Test Square update() with positional arguments"""
        square = Square(3, 2, 1, 5)

        square.update()
        self.assertEqual(square.id, 5)
        self.assertEqual(square.width, 3)
        self.assertEqual(square.height, 3)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 1)

        square.update(1)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.width, 3)
        self.assertEqual(square.height, 3)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 1)

        square.update(10, 5)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 1)

        square.update(0, 8, 7)
        self.assertEqual(square.id, 0)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 1)

        square.update(12, 10, 5, 7)
        self.assertEqual(square.id, 12)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)
        self.assertEqual(square.x, 5)
        self.assertEqual(square.y, 7)

        with self.assertRaises(ValueError):
            square.update(3, 12, 7, 15, 10, 11)

    def testSquareWithPositionalAndKeywordArguments(self):
        """Test Square update() with positional and keyword arguments"""
        square = Square(12, 7, 8, 5)

        square.update()
        self.assertEqual(square.id, 5)
        self.assertEqual(square.width, 12)
        self.assertEqual(square.height, 12)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

        square.update(20, 1, 2)
        self.assertEqual(square.id, 20)
        self.assertEqual(square.width, 1)
        self.assertEqual(square.height, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 8)

        square.update(size=30, id=3, y=10)
        self.assertEqual(square.id, 3)
        self.assertEqual(square.width, 30)
        self.assertEqual(square.height, 30)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 10)

        square.update(6, 50, 5, 3, size=45, id=16, x=0)
        self.assertEqual(square.id, 6)
        self.assertEqual(square.width, 50)
        self.assertEqual(square.height, 50)
        self.assertEqual(square.x, 5)
        self.assertEqual(square.y, 3)

        square.update(1, 30, **{"x": 0, "y": 1})
        self.assertEqual(square.id, 1)
        self.assertEqual(square.width, 30)
        self.assertEqual(square.height, 30)
        self.assertEqual(square.x, 5)
        self.assertEqual(square.y, 3)

    def testSquareToDictionary(self):
        """Test Square dictionnary representation"""
        square = Square(75, 1, 1)
        square.update(id=0)
        expected = {'size': 75, 'x': 1, 'y': 1, 'id': 0}
        self.assertEqual(square.to_dictionary(), expected)
        self.assertEqual(type(square.to_dictionary()), dict)

        square = Square(size=17, id=18)
        expected = {'size': 17, 'x': 0, 'y': 0, 'id': 18}
        self.assertEqual(square.to_dictionary(), expected)
        self.assertEqual(type(square.to_dictionary()), dict)

        square1 = Square(size=25, x=1, y=3, id=18)
        square2 = Square(25, 1, 3, 18)
        expected = {'size': 25, 'x': 1, 'y': 3, 'id': 18}
        self.assertEqual(square1.to_dictionary(), expected)
        self.assertEqual(type(square1.to_dictionary()), dict)
        self.assertEqual(square2.to_dictionary(), expected)
        self.assertEqual(type(square2.to_dictionary()), dict)

        square1 = Square(size=17, id=18)
        square2 = Square(17, 0, 0, 18)
        square2.update(45)
        expected = {'size': 17, 'x': 0, 'y': 0, 'id': 18}
        self.assertEqual(square1.to_dictionary(), expected)
        self.assertEqual(type(square1.to_dictionary()), dict)
        self.assertNotEqual(square2.to_dictionary(), expected)
        self.assertEqual(type(square2.to_dictionary()), dict)
