#!/usr/bin/python3
"""Create a rectangle class"""


class Rectangle:
    """Defines a rectangle class
    Attributes:
        number_of_instances (int): number of instances of rectangles
        print_symbol: symbol for string representation
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle class
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Deletes a rectangle instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__width + self.__height) * 2)

    def __str__(self):
        """Defines the print representation of rectangle class"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "\n".join(str(self.print_symbol) * self.__width
                             for i in range(self.__height))

    def __repr__(self):
        """Returns a representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares two rectangles and returns the biggest one"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size
        """
        return cls(size, size)
