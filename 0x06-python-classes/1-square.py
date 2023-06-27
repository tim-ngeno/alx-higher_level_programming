#!/usr/bin/python3
"""Creates a class Square"""


class Square:
    """Defines a square based on 0-square.py

    Attributes:
        __size (int): dimension of square
    """

    def __init__(self, size):
        """Initializes class Square
        Args:
            size (int): dimension of a side of a square
        """
        self.__size = size
