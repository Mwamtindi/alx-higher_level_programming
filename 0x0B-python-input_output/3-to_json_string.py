#!/usr/bin/python3
"""A module that defines to_json_string function."""


import json

def to_json_string(my_obj):
    """Returns JSON rep of an object"""
    return json.dumps(my_obj)
