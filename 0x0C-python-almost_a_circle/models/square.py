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
        super().__init__(self.size, self.size, x, y, id)

    @property
    def size(self):
        """Return the size of the square

        :return: the square's size
        :rtype: int
        """
        return self.width

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

        self.width = value
        self.height = value

    def __str__(self):
        """Human readable representation of Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Update the square's attributes

        :param args: new values of square attributes
        :type args: tuple
        :param kwargs: key:value values
        :type kwargs: dict
        """
        if args is not None and len(args) != 0:
            if len(args) == 1:
                self.id, = args
            elif len(args) == 2:
                self.id, self.size = args
            elif len(args) == 3:
                self.id, self.size, self.x = args
            elif len(args) >= 4:
                self.id, self.size, self.x, self.y = args
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
