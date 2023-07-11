#!/usr/bin/python3
"""implementation of class Student"""


class Student:
    """A class Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize class instance """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary representation of a
        Student instance
        """
        if (type(attrs) == list and
                (all(type(i) == str for i in attrs))):
            return {a: getattr(self, a) for a in attrs
                    if hasattr(self, a)}
        return (self.__dict__)

    def reload_from_json(self, json):
        """Replaces all attributes of Student instance"""
        {setattr(self, key, json[key]) for key in json}
