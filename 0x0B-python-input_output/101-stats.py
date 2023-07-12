#!/usr/bin/python3
"""Log parsing"""

import sys

status_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

i = 0
size = 0

try:
    for content in sys.stdin:
        line = content.split()
        if (line[-2]) in status_count:
            status_count[line[-2]] += 1
            i += 1
            size += int(line[-1])
        if i % 10 == 0:
            print("File size: {:d}".format(size))
            for key, value in sorted(status_count.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(size))
    for key, value in sorted(status_count.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(size))
    for key, value in sorted(status_count.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
