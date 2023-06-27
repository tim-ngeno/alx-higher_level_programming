#!/usr/bin/python3
"""Create a class that defines the area of a square"""


class Square:
    """defines a square based on 2-square.py

    Attributes:
        __size (int): dimension of the square
    """

    def __init__(self, size=0):
        """Initializes a Square object
        Args:
            size (int): dimension of the square
        """
        self.__size = size
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates the area of a square

        Returns:
            current square area
        """
        return self.__size * self.__size
