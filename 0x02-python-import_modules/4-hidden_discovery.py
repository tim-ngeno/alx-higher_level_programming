#!/usr/bin/python3
from inspect import getmembers, isfunction
import hidden_4

if __name__ == "__main__":
    print(getmembers(hidden_4, isfunction))
