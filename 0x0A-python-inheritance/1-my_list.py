#!/usr/bin/python3
"""Defines class MyList inherited list"""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
