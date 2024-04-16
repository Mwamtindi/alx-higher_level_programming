#!/usr/bin/python3
"""A module that defines student based on 10-student.py method."""


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
        - dict: A dictionary rep of Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {r: getattr(self, r) for r in attrs if hasattr(self, r)}

    def reload_from_json(self, json):
        """
        Replace all attrs of Student instance with the values from a dict.

        Args:
        - json: A dictionary containing attr names and values.

        """
        for key, value in json.items():
            setattr(self, key, value)
