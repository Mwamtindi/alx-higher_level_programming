#!/usr/bin/python3
"""A module that defines class_to_json function."""


def class_to_json(obj):
    """Returns dictionary desc with simple data structure."""
    attr = obj.__dict__

    s_attr = {
        key: value for key, value in attr.items()
        if isinstance(value, (list, dict, str, int, bool))
    }

    return s_attr
