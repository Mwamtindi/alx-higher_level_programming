#!/usr/bin/python3
"""A module that defines save_to_json_file function."""


import json
"""Import json module."""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using json rep."""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
