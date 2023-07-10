#!/usr/bin/python3
"""Implementing inheritance in a class Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square based on base class Rectangle"""

    def __init__(self, size):
        """Initializes the class Square with size
        Args:
            size (int): the square dimension
        """
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """Calculates the area of a square"""
        return (self.__size ** 2)

    def __str__(self):
        """Defines the print representation of class Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
