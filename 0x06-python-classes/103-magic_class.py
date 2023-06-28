#!/usr/bin/python3
"""disassembly of python bytecode"""
import math


class MagicClass:
    """Defines a magic class that performs operations on a circle"""

    def __init__(self, radius=0):
        """Initializes the magic class"""
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """calculates the area of a circle"""
        return (math.pi * (self.__radius ** 2))

    def circumference(self):
        """calculates the circumference of the circle"""
        return (math.pi * (self.__radius * 2))
