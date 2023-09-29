#!/usr/bin/python3
"""
Send a POST request to a URL with an email as parameter
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url_address = sys.argv[1]
    value = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')

    request = urllib.request.Request(url_address, data)
    with urllib.request.urlopen(request) as response:
        body = response.read().decode('UTF-8')

        print(body)
