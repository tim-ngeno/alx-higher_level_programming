#!/usr/bin/python3
import sys

if __name__ == "__main__":
    count = len(sys.argv[1:])
    if count == 0:
        print("{} arguments.".format(count))
    else:
        if count == 1:
            print("{} argument:".format(count))
        else:
            print("{} arguments:".format(count))
        for i, arg in enumerate(sys.argv[1:]):
            print("{}:".format(i + 1), arg)
