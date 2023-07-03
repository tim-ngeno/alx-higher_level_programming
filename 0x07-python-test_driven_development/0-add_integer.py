#!/usr/bin/python3
"""
    Adds two integers and returns the sum
"""


def add_integer(a, b=98):
    """Adds two integers
    Args:
        a (int): first integer
        b (int): second integer

    Return:
        result of addition of two integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return (a + b)
