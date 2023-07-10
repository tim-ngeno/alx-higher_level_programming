#!/usr/bin/python3
"""check instance of inherited class(direct/indirect)"""


def inherits_from(obj, a_class):
    """Checks if object is an inherited instance of specified
    class (directly or indirectly)

    Args:
        obj: object argument
        a_class: class instance
    Return:
        True: if object is instance of inherited class
        False: if not instance of inherited class
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
