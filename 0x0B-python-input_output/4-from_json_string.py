#!/usr/bin/python3
"""deserialize JSON object"""
import json


def from_json_string(my_str):
    """Returns a Python object represented by a JSON string

    Args:
        my_str (str): JSON string
    """
    return json.loads(my_str)
