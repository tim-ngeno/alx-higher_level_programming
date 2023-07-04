#!/usr/bin/python3
"""Create a locked class with no class or object attribute"""


class LockedClass:
    """prevents the user from dynamically creating new instance
    attributes, except if attribute == first_name
    """
    __slots__ = ["first_name"]
