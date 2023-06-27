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
        self.size = size

    @property
    def size(self):
        """
        defines the getter for the square size
        Returns:
            size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """defines the setter property
        Args:
            value (int): size of the square
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of a square

        Returns:
            current square area
        """
        return self.__size * self.__size
