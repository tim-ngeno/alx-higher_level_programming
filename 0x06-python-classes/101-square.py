#!/usr/bin/python3
"""Create a class that defines the area of a square"""


class Square:
    """defines a square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square object
        Args:
            size (int): dimension of the square
            position (int, int): coordinates of new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        defines the getter/setter for the square size
        Returns:
            size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves the position argument and sets it"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (len(value) != 2 or
            not isinstance(value, tuple) or
            not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of a square

        Returns:
            current square area
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square  with a '#' character"""
        if self.__size == 0:
            print()
            return
        [print() for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for k in range(0, self.__position[0])]
            [print("#", end="") for m in range(0, self.__size)]
            print()

    def __str__(self):
        """Prints the square  with a '#' character"""
        if self.__size == 0:
            print()
            return
        [print() for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for k in range(0, self.__position[0])]
            [print("#", end="") for m in range(0, self.__size)]
            if i != self.__size - 1:
                print()
        return ("")
