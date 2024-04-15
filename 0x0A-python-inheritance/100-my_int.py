#!/usr/bin/python3
"""
Module containing class MyInt
"""


class MyInt(int):
    """MyInt is a rebel"""
    def __new__(cls, *args, **kwargs):
        """creating a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != before is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == before is now !="""
        return int(self) == other
