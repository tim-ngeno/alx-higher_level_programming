#!/usr/bin/python3
"""Create a rectangle class"""


class Rectangle:
    """Defines a rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle class
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Defines the getter/setter for the rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Defines getter/setter for the rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be  >= 0")
        self.__height = value
