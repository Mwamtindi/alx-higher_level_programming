#!/usr/bin/python3
"""A module that defines load_from_json_file function."""


import json
"""Import json module."""


def load_from_json_file(filename):
    """Creates an object from a json file."""
    with open(filename, "r") as file:
        return json.load(file)
