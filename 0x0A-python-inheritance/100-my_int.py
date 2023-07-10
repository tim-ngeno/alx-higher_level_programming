#!/usr/bin/python3
"""Inheritance implementation"""


class MyInt(int):
    """A class MyInt"""

    def __new__(cls, *args, **kwargs):
        """Create a new instance of a class cls
        """
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, x):
        """Change the double_equals to '!='
        """
        return int(self) != x

    def __ne__(self, x):
        """Change the '!=' to  '=='
        """
        return int(self) == x
