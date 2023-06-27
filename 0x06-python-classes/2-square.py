#!/usr/bin/python3
"""creates the definition of a class square"""


class Square:
    """Defines a class Square

    Attributes:
        __size (int): dimension of a side of the square
    """

    def __init__(self, size=0):
        """Initializes a square object
        Args:
            size (int): dimension of square
        """
        self.__size = size
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
