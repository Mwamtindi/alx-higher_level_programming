#!/usr/bin/python3
"""A module that defines append_write function."""


def append_write(filename="", text=""):
    """Appends string at the end of file and returns num of chars added"""
    with open(filename, "a", encoding="utf-8") as file:
        char_n_added = file.write(text)
    return char_n_added
