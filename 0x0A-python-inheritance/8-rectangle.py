#!/usr/bin/python3
"""Module that defines Rectangle class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass rectangle of class BaseGeometry."""
    def __init__(self, width, height):
        """A constructor."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
