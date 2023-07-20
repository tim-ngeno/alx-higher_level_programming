#!/usr/bin/python3
""" The square module """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ A class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Defines the class constructor
        Args:
            size (int): dimensnion of the square
            x (int): x vector position
            y (int): y vector position
            id (int): the id
        """

        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Defines the getter and setter methods for the width"""
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Assigns attributes to the list of arguments """
        attributes = ['id', 'size', 'x', 'y']
        if args and len(args) != 0:
            for index, arg in enumerate(args):
                if index < len(attributes):
                    setattr(self, attributes[index], arg)
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Returns the dictionary representation
        of a square instance"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y,
        }

    def __str__(self):
        """ Defines the print representation of a square instance"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size
        )
