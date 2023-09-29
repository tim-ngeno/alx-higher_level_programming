#!/usr/bin/python3
"""
Send a request to a URL and display the value of the
`X-Request-Id` variable found in the response
"""

import sys
import urllib.request

url_address = sys.argv[1]

with urllib.request.urlopen(url_address) as res:
    headers = res.info()

    # Check for desired header
    x_request_id = headers.get('X-Request-Id')
    print(x_request_id)
