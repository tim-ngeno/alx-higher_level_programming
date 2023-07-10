#!/usr/bin/python3
""" a function to list attributes and methods of an object """


def lookup(obj):
    """Defines a function that retrieves available attributes
    and methods of an object

    Args:
        obj: an object input
    Return:
        a list of available attributes and methods
    """
    return dir(obj)
