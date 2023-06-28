#!/usr/bin/python3
""" defines a square shape """


class Square:
    """ represents square with private instance attribute size """

    def __init__(self, size=0):
        """
        initializes a square object
        Args:
            size (int): size of square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
