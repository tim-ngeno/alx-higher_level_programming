#!/usr/bin/python3
"""
Send a POST request with parameters
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    value = {"email": email}
    res = requests.post(url, data=value)
    print(res.text)
