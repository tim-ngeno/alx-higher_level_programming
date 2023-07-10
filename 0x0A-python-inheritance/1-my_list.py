#!/usr/bin/python3
"""Inheritance implementation"""


class MyList(list):
    """A class MyList"""

    def print_sorted(self):
        """Defines a method that print the list, in sorted order
        """
        print(sorted(self))
