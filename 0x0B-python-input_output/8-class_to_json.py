#!/usr/bin/python3
"""Return a dictionary description"""


def class_to_json(obj):
    """Defines a function that returns the dictionary description
    with simple data structures
    Args:
        obj (cls): an instance of a class
    """
    return (obj.__dict__)
