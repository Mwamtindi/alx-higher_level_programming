#!/usr/bin/python3
"""Module that defines Rectangle class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A suclass square of class rectangle."""
    def __init__(self, size):
        """A constructor."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method to calculate area of square."""
        return self.__size ** 2

    def __str__(self):
        """Returns  string representation of the square."""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
