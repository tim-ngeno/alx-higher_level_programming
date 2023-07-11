#!/usr/bin/python3
"""Reading from a file"""


def read_file(filename):
    """Reads from a file and print it to stdout

    Args:
        filename: specifies the path of the file
    """
    with open(filename, "r") as file:
        content = file.read()
        print(content, end="")
