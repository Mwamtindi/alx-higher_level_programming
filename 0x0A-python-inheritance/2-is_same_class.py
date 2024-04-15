#!/usr/bin/python3
"""Module that defines is_same_class function"""


def is_same_class(obj, a_class):
    """If obj is exactly an instance of a_class returns True.
    otherwise False."""
    return type(obj) == a_class
