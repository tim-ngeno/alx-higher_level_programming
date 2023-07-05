#!/usr/bin/python3
"""
define a function to print a square
"""


def print_square(size):
    """prints a square with the character '#'
    Args:
        size (int): dimension of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
