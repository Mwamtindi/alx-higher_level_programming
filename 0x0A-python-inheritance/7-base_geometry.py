#!/usr/bin/python3
"""Module that defines BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry class based on 5-base_geometry.py."""
    def area(self):
        """Using method to compute area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method used to  validate the value."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
