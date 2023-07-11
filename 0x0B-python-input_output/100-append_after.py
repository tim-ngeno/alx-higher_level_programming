#!/usr/bin/python3
"""File manipulation"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after specific string"""
    with open(filename, "r") as file:
        wordlist = []
        while True:
            line = file.readline()
            if line == "":
                break
            wordlist.append(line)
            if search_string in line:
                wordlist.append(new_string)
    with open(filename, "w") as file:
        file.writelines(wordlist)
