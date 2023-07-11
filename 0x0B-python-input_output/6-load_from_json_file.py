#!/usr/bin/python3
"""create object from a JSON file"""
import json


def load_from_json_file(filename):
    """Defines a function to create an object from a JSON file

    Args:
        filename: file path
    """
    with open(filename, "r") as file:
        json.load(file)
