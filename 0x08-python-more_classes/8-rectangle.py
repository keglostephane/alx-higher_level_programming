#!/usr/bin/python3
"""A module that allow to work with rectangle.
"""


class Rectangle:
    """Define a rectangle.

    :param number_of_instances: number of ``Rectangle`` objects
    :type number_of_instances: int
    :param print_symbol: symbol used to print the rectangle
    :type print_symbol: any
    :param width: width of the rectangle, defaults to 0
    :type with: int, optional
    :raises TypeError: width must be an integer
    :raises ValueError: width must be >= 0
    :param height: height of the rectangle, defaults to 0
    :type height: int, optional
    :raises TypeError: height must be an integer
    :raises ValueError: height must be >= 0
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle.

        :return: the actual size of the rectangle.
        :rtype: int
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        :param value: value of the rectangle
        :type value: int
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.

        :return: the actual height of the rectangle
        :rtype: int
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        :param value: the height of the rectangle
        :type value: int
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return the rectangle area.

        :return: the rectangle area
        :rtype: int
        """
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle perimeter.

        :return: the rectanglr perimeter
        :rtype: int
        """
        if not self.__width or not self.__height:
            return 0

        return (self.__width + self.__height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on the area.

        :param rect_1: first rectangle
        :type rect_1: Rectangle
        :raises TypeError: rect_1 must be an instance of Rectangle
        :param rect_2: second rectangle
        :type rect_2: Rectangle
        :raises TypeError: rect_2 must be an instance of Rectangle
        :return: the biggest rectangle
        :rtype: Rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __str__(self):
        """Human readable representation of the rectangle.
        """
        if not self.__width or not self.__height:
            return ""

        return (str(self.print_symbol) * self.__width + "\n") * \
            (self.__height - 1) + str(self.print_symbol) * self.__width

    def __repr__(self):
        """String representation of the rectangle.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Delete the rectangle.
        """
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
