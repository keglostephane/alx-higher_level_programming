#!/usr/bin/python3
"""Rectangle class module
"""
from models.base import Base


class Rectangle(Base):
    """A Rectangle class.

    :param width: width of the rectangle
    :type witdh: int
    :param height: height of the rectangle
    :type height: int
    :param x: position on X-axis
    :type x: int
    :param y: postion on Y-axis
    :type y: int
    :param id: id value of the rectangle
    :type id: int
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle initializer"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Return width of the rectangle.

        :return: the width of the rectangle
        :rtype: int
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        :param value: value of rectangle's width
        :type value: int
        """
        self.__width = value

    @property
    def height(self):
        """Return the height of the rectangle.

        :return: the height of the rectangle
        :rtype: int
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        :param value: value of the rectangle's height
        :type value: int
        """
        self.__height = value

    @property
    def x(self):
        """Return rectangle position on X-axis.

        :return: the position on X-axis
        :rtype: int
        """
        return self.__x

    @x.setter
    def x(self, value):
        """set rectangle position on X-axis.

        :param value: postion on X-axis
        :type value: int
        """
        self.__x = value

    @property
    def y(self):
        """Return rectanglr position on Y-axis.

        :return: the position on Y-axis
        :rtype: int
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Set rectangle position on Y-axis.

        :param value: position of Y-axis
        :type value: int
        """
        self.__y = value
