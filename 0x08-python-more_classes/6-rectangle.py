#!/usr/bin/python3
"""A module containing rectangle class"""


class Rectangle:
    """Class defining rectangle based on 4-rectangle.py"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Width and height initialization"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter method"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns back area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns back perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns rectangle string representation"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        """Returns rectangle string representation for recreation"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Printed message when  Rectangle instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
