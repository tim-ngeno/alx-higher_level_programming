#!/usr/bin/python3
"""a child class of the Base class"""

from models.base import Base


class Rectangle(Base):
    """A class Rectangle inheriting Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor
        Args:
            width (int): rectangle width
            height (int): rectangle height
            x: value of x
            y: value of y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Defines the getter and setter methods for the width
        Getter method returns the value of the width
        Setter method validates the type and value
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Defines the getter and setter methods for the height
        Getter method returns the value of the height
        Setter method validates the value and type of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Defines the getter and setter methods for x
        Getter method returns the value of x
        Setter method validates the type and value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Defines the getter and setter methods for y
        Getter method returns the value of y
        Setter method validates type and value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle
        Return:
            Area of the rectangle instance
        """
        return (self.__width * self.__height)

    def display(self):
        """Displays the rectangle instance with the char '#' """
        for y in range(self.__y):
            print()

        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)
            # print(''.join(' ' for x in range(1, self.__x)) +
            #       ''.join('#' for y in range(self.__width)))

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) != 0:
            for idx, arg in enumerate(args):
                if idx < len(attributes):
                    setattr(self, attributes[idx], arg)

        for key in kwargs:
            setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Returns the dictionary representation of
        rectangle instance
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y,
        }

    def __str__(self):
        """Defines the print representation of a rectangle instance
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y,
            self.__width, self.__height
        )
