#!/usr/bin/python3
"""Compare object instance and class values
"""


def is_kind_of_class(obj, a_class):
    """check if obj is an instance of, or obj is instance
    of the inherited class

    Args:
        obj: object argument
        a_class: class instance
    Return:
        True: if is an instance
        False: if not an instance of class, or subclass
    """
    return isinstance(obj, a_class)
