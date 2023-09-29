#!/usr/bin/python3
"""
Display the value of the variable `X-Request-Id` in the response
header
"""

import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    response = requests.get(url)
    data = response.headers

    x_request_id = data.get('X-Request-Id')
    print(x_request_id)
