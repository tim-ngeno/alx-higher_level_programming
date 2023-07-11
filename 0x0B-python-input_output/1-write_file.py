#!/usr/bin/python3
"""Writing to a file"""


def write_file(filename="", text=""):
    """Writes the content of `text` to `filename`

    Args:
        filename: path to the input file
        text (str): string to be written to filename
    """
    with open(filename, "w") as file:
        chars = file.write(text)
    return chars
