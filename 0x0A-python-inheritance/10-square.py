#!/usr/bin/python3
"""Implement inheritance in a square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square from super class Rectangle"""

    def __init__(self, size):
        """Initializes a square with the dimension size
        Args:
            size (int/float): dimension of the square
        """
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """Calculates the area of the square"""
        return (self.__size ** 2)

    def __str__(self):
        """defines the print representation"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
