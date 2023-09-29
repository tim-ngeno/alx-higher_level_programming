#!/usr/bin/python3
"""
Using urllib to perform a GET request
"""

import urllib.request

hbtn_url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(hbtn_url) as req:
    response = req.read()

print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(
    type(response), response, response.decode('UTF-8')
))
