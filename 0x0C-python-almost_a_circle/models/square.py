#!/usr/bin/python3
"""Square class module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class.

    :param width: width of the Square
    :type witdh: int
    :param height: height of the Square
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
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Human readable representation of Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
