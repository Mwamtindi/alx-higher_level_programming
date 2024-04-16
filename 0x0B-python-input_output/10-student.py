#!/usr/bin/python3
"""A module that contains Student class."""


class Student:
    """The Student class."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary rep of Student instance.

        Args:
        - attrs: List of attr names to retrieve.
            If None, retrieve all attrs.

        Returns:
        - dict: A dictionary rep of  Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
