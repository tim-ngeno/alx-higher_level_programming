#!/usr/bin/python3
"""
Prints the full name passed as arguments
"""


def say_my_name(first_name, last_name=""):
    """Returns the first and last name in a string
    Args:
        first_name (str): first name argument
        last_name (str): last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    return "My name is {} {}".format(first_name, last_name)
