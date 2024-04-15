#!/usr/bin/python3


def lookup(obj):
    """Returns a list of attributes and methods of an object."""
    return dir(obj)

# Example usage
class Cybertawk:
    def __init__(self):
        self.attribute1 = 1

    def method1(self):
        pass

obj = Cybertawk()
print(lookup(obj))
