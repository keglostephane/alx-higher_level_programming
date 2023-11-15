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

    def testRectangleDisplay(self):
        """Test printing Rectangle"""
        with patch('sys.stdout', new_callable=StringIO) as output:
            rect = Rectangle(4, 3)
            rect.display()
            result = output.getvalue()
            expected = ("####\n"
                        "####\n"
                        "####\n")
            self.assertEqual(result, expected)

        with patch('sys.stdout', new_callable=StringIO) as output:
            rect = Rectangle(1, 1)
            rect.display()
            result = output.getvalue()
            expected = ("#\n")
            print("\nCalling display() method of Rectangle(1, 1)")
            print(result)
            self.assertEqual(result, expected)

        with patch('sys.stdout', new_callable=StringIO) as output:
            rect = Rectangle(2, 3)
            rect.display()
            result = output.getvalue()
            expected = ("##\n"
                        "##\n"
                        "##\n")
            self.assertEqual(result, expected)

    def testRectangleStr(self):
        """Test human readable representation of Rectangle"""
        with patch('sys.stdout', new_callable=StringIO) as output:
            rect = Rectangle(4, 3, 2, 1, 0)
            print(rect)
            result = output.getvalue()
            expected = "[Rectangle] (0) 2/1 - 4/3\n"
            self.assertEqual(result, expected)

        with patch('sys.stdout', new_callable=StringIO) as output:
            rect = Rectangle(1, 5, 0, 0, 6)
            print(rect)
            result = output.getvalue()
            expected = "[Rectangle] (6) 0/0 - 1/5\n"
            self.assertEqual(result, expected)

    def testRectangleDisplayWithCoordinates(self):
        """Test printing of Rectangle using coordinates"""
        with patch('sys.stdout', new_callable=StringIO) as output:
            rect = Rectangle(6, 5, 2, 1, 1)
            rect.display()
            result = output.getvalue()
            expected = ("\n"
                        "  ######\n"
                        "  ######\n"
                        "  ######\n"
                        "  ######\n"
                        "  ######\n")
            self.assertEqual(result, expected)

        with patch('sys.stdout', new_callable=StringIO) as output:
            rect = Rectangle(2, 3, 0, 0, 5)
            rect.display()
            result = output.getvalue()
            expected = ("##\n"
                        "##\n"
                        "##\n")
            self.assertEqual(result, expected)

        with patch('sys.stdout', new_callable=StringIO) as output:
            rect = Rectangle(1, 1, 3, 5, 23)
            rect.display()
            result = output.getvalue()
            expected = ("\n"
                        "\n"
                        "\n"
                        "\n"
                        "\n"
                        "   #\n")
            self.assertEqual(result, expected)

    def testRectangleUpdateWithPositionalArguments(self):
        """Test Rectangle update() with positional arguments"""
        rect = Rectangle(7, 3, 0, 0, 1)

        rect.update()
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 1)

        rect.update(15)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 15)

        rect.update(15, 9)
        self.assertEqual(rect.width, 9)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 15)

        rect.update(23, 17, 2)
        self.assertEqual(rect.width, 17)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 23)

        rect.update(6, 23, 8, 7)
        self.assertEqual(rect.width, 23)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 7)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 6)

        rect.update(23, 17, 3, 5, 99)
        self.assertEqual(rect.width, 17)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 99)
        self.assertEqual(rect.id, 23)

        with self.assertRaises(ValueError):
            rect.update(2, 7, 9, 6, 3, 16)

    def testRectangleUpdateWithPositionalAndKeywordArguments(self):
        """Test Rectangle update() with positional and keyword arguments"""
        rect = Rectangle(19, 15, 5, 3, 23)

        rect.update()
        self.assertEqual(rect.width, 19)
        self.assertEqual(rect.height, 15)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 23)

        rect.update(78, 2, 7)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 78)

        rect.update(id=8, x=3, y=10)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 10)
        self.assertEqual(rect.id, 8)

        rect.update(21, 14, 13, 7, id=10, y=20, width=17)
        self.assertEqual(rect.width, 14)
        self.assertEqual(rect.height, 13)
        self.assertEqual(rect.x, 7)
        self.assertEqual(rect.y, 10)
        self.assertEqual(rect.id, 21)

        rect.update(*(), **{"width": 16, "height": 10})
        self.assertEqual(rect.width, 16)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 7)
        self.assertEqual(rect.y, 10)
        self.assertEqual(rect.id, 21)

        rect.update(widht=27, height=2, z=50)
        self.assertEqual(rect.width, 16)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 7)
        self.assertEqual(rect.y, 10)
        self.assertEqual(rect.id, 21)

    def testRectangleToDictionary(self):
        """Test Rectangle dictionnary representation"""
        rect = Rectangle(75, 25, 1, 1, 1)
        expected = {'width': 75, 'height': 25, 'x': 1, 'y': 1, 'id': 1}
        self.assertEqual(rect.to_dictionary(), expected)
        self.assertEqual(type(rect.to_dictionary()), dict)

        rect = Rectangle(width=17, height=13, id=18)
        rect.update(14, 5)
        expected = {'width': 5, 'height': 13, 'x': 0, 'y': 0, 'id': 14}
        self.assertEqual(rect.to_dictionary(), expected)
        self.assertEqual(type(rect.to_dictionary()), dict)

        rect1 = Rectangle(width=17, height=13, id=18)
        rect2 = Rectangle(17, 13, 0, 0, 18)
        expected = {'width': 17, 'height': 13, 'x': 0, 'y': 0, 'id': 18}
        self.assertEqual(rect1.to_dictionary(), expected)
        self.assertEqual(type(rect1.to_dictionary()), dict)
        self.assertEqual(rect2.to_dictionary(), expected)
        self.assertEqual(type(rect2.to_dictionary()), dict)

        rect1 = Rectangle(width=17, height=13, id=18)
        rect2 = Rectangle(17, 13, 1, 0, 18)
        expected = {'width': 17, 'height': 13, 'x': 0, 'y': 0, 'id': 18}
        self.assertEqual(rect1.to_dictionary(), expected)
        self.assertEqual(type(rect1.to_dictionary()), dict)
        self.assertNotEqual(rect2.to_dictionary(), expected)
        self.assertEqual(type(rect2.to_dictionary()), dict)
