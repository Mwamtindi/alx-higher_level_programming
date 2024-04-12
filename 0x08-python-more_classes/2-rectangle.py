#!/usr/bin/python3
"""module with class that defines a rectangle based on 1-rectangle.py"""


class Rectangle:
    """Class defining rectangle based on 1-rectangle"""

    def __init__(self, width=0, height=0):
        """Width and height initialization"""
        self.width = width
        self.height = height

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
