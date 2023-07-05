#!/usr/bin/python3
"""Print text with 2 new lines after '.', '?', ':' """


def text_indentation(text):
    """
    Print text with 2 new lines after '.', '?', ':'

    Args:
        text (str): input text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        if char == "." or char == "?" or char == ":" or char == ",":
            print("\n")
        else:
            print(char, end="")
