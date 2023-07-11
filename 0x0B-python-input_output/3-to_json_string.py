#!/usr/bin/python3
"""JSON representation"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of a string

    Args:
        obj (str): input string to be converted
    Return:
        converted JSON output
    """
    return json.dumps(my_obj)
