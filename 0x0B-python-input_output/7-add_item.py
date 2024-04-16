#!/usr/bin/python3
"""A module that adds all arguments to a python list and save them."""


import sys


from 5-save_to_json_file.py import save_to_json_file
from 6-load_from_json_file.py import load_from_json_file

try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []
items.extend(sys.argv[1:])
save_to_json_file(items, "add_item.json")