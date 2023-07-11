#!/usr/bin/python3
"""append data to a file"""


def append_write(filename="", text=""):
    """Appends data to the end of a file
    Args:
        filename (str): path to the file
        text (str): data to be added to file
    Return:
        chars: the number of characters added
    """
    with open(filename, "a") as file:
        chars = file.write(text)

    return chars
