#!/usr/bin/python3
"""Module for MyList inherited list"""


class MyList(list):
    """MyList class."""
    def print_sorted(self):
        """Method to print sorted list."""
        print(sorted(self))
