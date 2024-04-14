#!/usr/bin/python3
"""Module that prints first and last name or both"""


def say_my_name(first_name, last_name=""):
    """
        Args:
            first_name and last_name are strings
        Otherwise:
            TypeError: first_name must be a string,
                      last_name must be a string
        """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
