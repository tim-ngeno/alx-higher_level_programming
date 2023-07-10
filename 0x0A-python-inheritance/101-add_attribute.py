#!/usr/bin/python3
"""Add attribute"""


def add_attribute(obj, attribute, value):
    """Adds an attribute to an object if possible
    Args:
        obj (any): object argument
        attribute (str): attribute name
        value (any): data value of attribute
    Raises:
        TypeError: if the attribute cannot be added
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
