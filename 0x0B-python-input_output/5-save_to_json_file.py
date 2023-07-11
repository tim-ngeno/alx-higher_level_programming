#!/usr/bin/python3
"""Use JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation

    Args:
        my_obj: object file to be converted to JSON string
        filename: file path
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
