#!/usr/bin/python3
"""Create a class Base
"""
import json


class Base:
    """Defines the Base class
    Attributes:
        __nb_objects (int): defines number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor
        Args:
            id (int): the id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation
        of list_dictionaries
        Args:
            list_dictionaries: a list of dictionaries
        """
        return "[]" if list_dictionaries is None else json.dumps(
            list_dictionaries
        )

    @staticmethod
    def from_json_string(json_string):
        """ Returns a list of JSON string format of `json_string`
        Args:
            json_string (str): string representing a list of
            dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of list_objs to a file

        Args:
            list_objs (list): list of instances(child class) of Base
        """
        if list_objs is None:
            objs = []
        else:
            as_dict = [obj.to_dictionary() for obj in list_objs]
            objs = cls.to_json_string(as_dict)
            # objs = cls.to_json_string(as_dict)
        with open("{}.json".format(cls.__name__), "w") as file:
            json.dump(objs, file)
            # dumping twice leads to escape characters being
            # appended in the string

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1, 1, 1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1, 1, 1, 1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        try:
            with open("{}.json".format(cls.__name__), "r") as file:
                content = file.read()
                if content:
                    obj_list = cls.from_json_string(content)
                    instances = [cls.create(**obj) for obj in
                                 obj_list]
                    return instances
                else:
                    return []
        except FileNotFoundError:
            return []
