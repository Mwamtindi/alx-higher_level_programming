#!/usr/bin/python3
"""A module that defines read_file function."""


def read_file(filename=""):
    """Reads a text file and prints it to stdout."""
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end='')
