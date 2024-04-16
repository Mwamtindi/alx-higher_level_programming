#!/usr/bin/python3
"""A module that defines write_file function."""


def write_file(filename="", text=""):
    """Writes a string and returns the numb of chars written"""
    with open(filename, "w", encoding="utf-8") as file:
        char_n_written = file.write(text)
    return char_n_written
