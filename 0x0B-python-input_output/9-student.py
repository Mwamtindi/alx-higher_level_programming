#!/usr/bin/python3
"""A module that contains class Student."""


class Student:
    """The student class."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Return a dictionary rep of Student instance.

        Returns:
        - dict: A dictionary rep of Student instance.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
