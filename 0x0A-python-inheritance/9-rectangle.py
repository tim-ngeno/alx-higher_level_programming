#!/usr/bin/python3
"""Create a subclass Rectangle based on
module 7-base_geometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a class Rectangle, sharing
    attributes of BaseGeometry"""

    def __init__(self, width, height):
        """Initializes class base geometry"""
        BaseGeometry.__init__(self)
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Defines the print representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
