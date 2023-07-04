#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """
    Resticts the user from dynamically creating new instance attributes,
    except if the new instance attribute is named first_name.
    """
    __slots__ = ["first_name"]
