#!/usr/bin/python3
"""Module that defines a function to add attributes to objects."""


def add_attribute(obj, att, value):
    """Adding new attribute to an object if possible.
    Args:
        obj (any): The object where attribute is added.
        att (str): The name of the attr to add to obj.
        value (any): The value of attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
