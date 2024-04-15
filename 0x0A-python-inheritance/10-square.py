#!/usr/bin/python3
"""Module that defines Rectangle class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A subclass square of class rectangle."""
    def __init__(self, size):
        """A constructor."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method that returns area of square."""
        return self.__size ** 2
