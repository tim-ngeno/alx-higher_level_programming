#!/usr/bin/python3
"""Check object type"""


def is_same_class(obj, a_class):
    """Compares obj and an instance of a_class

    Args:
        obj: object argument
        a_class: class argument
    Return:
        True: if obj is exactly an instance of a_class
        False otherwise
    """
    return (type(obj) == a_class)
