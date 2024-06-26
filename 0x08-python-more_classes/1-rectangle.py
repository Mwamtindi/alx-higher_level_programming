#!/usr/bin/python3
"""A module containing rectangle class"""


class Rectangle:
    """Class defining rectangle based on 0-rectangle.py"""

    def __init__(self, width=0, height=0):
        """ width and height initialization"""
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
