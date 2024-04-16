#!/usr/bin/python3
"""A module that defines append_after function."""


def append_after(filename="", search_string="", new_string=""):
    """
    Append line of text after each line containing specific string in a file.

    Args:
    - filename: Name of the file to modify.
    - search_string: String to search for in each line.
    - new_string: String to append after each line containing search string.
    """
    text = ""
    with open(filename, "r") as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w") as w:
        w.write(text)
