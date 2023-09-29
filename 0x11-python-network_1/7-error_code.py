#!/usr/bin/python3
"""Managing errors and exceptions"""

import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    res = requests.get(url)

    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    print(res.text)
