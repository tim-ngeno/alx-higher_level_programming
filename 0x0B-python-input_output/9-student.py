#!/usr/bin/python3
"""implementation of class student"""


class Student:
    """A class Student"""

    first_name = ""
    last_name = ""
    age = None

    def __init__(self, first_name, last_name, age):
        """Initialize class instance """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve dictionary representation of a
        Student instance
        """
        return (self.__dict__)
