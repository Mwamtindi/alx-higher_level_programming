#!/usr/bin/python3
"""A module that defines from_json_string function."""


import json
"""Import json module"""


def from_json_string(my_str):
    """Returns python data structure represented by a JSON string."""
    return json.loads(my_str)
