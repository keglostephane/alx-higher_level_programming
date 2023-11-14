#!/usr/bin/python3
"""Square class module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class.

    :param size: size of the square
    :type size: int
    :param width: width of the Square, same as size
    :type witdh: int
    :param height: height of the Square, same as size
    :type height: int
    :param x: position on X-axis
    :type x: int
    :param y: postion on Y-axis
    :type y: int
    :param id: id value of the Square
    :type id: int
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Square initializer"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return the size of the square

        :return: the square's size
        :rtype: int
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square

        :param value: value of the square's size
        :type value: int
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__size = value
        self.width = value
        self.height = value

    def __str__(self):
        """Human readable representation of Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
